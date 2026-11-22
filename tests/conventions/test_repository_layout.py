"""Repository conventions that P0-01 sets up and later tasks must keep."""

import json
import re
import tomllib
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]

LAYOUT = [
    "apps/api",
    "apps/worker",
    "apps/web",
    "packages/core",
    "packages/contracts",
    "packages/engines/production",
    "packages/engines/transportation",
    "packages/engines/inventory",
    "packages/validators",
    "docs/prd",
    "docs/adr",
    "docs/tasks",
    "docs/data-dictionary",
    "docs/state-machines",
    "docs/engines",
    "docs/runbooks",
    "tests/reference-cases",
    "tests/e2e",
    "tests/security",
    "tests/performance",
    "infra",
]

COMPOSE_SERVICES = ["postgres", "api", "worker", "web", "mailpit", "minio"]
MAKE_TARGETS = ["dev", "test", "lint", "typecheck", "migrate", "bench"]
EXACT_NPM_VERSION = re.compile(r"^\d+\.\d+\.\d+$")


def _toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def _workspace_members() -> list[Path]:
    members: list[str] = _toml(ROOT / "pyproject.toml")["tool"]["uv"]["workspace"]["members"]
    return [ROOT / member for member in members]


def _python_requirements() -> list[tuple[Path, str]]:
    found: list[tuple[Path, str]] = []
    for pyproject in [ROOT / "pyproject.toml", *(m / "pyproject.toml" for m in _workspace_members())]:
        data = _toml(pyproject)
        requirements = list(data["project"].get("dependencies", []))
        for group in data.get("dependency-groups", {}).values():
            requirements.extend(group)
        requirements.extend(data.get("build-system", {}).get("requires", []))
        found.extend((pyproject, req) for req in requirements if not req.startswith("nasq-"))
    return found


def _npm_dependencies() -> dict[str, str]:
    package = json.loads((ROOT / "apps/web/package.json").read_text(encoding="utf-8"))
    return {**package.get("dependencies", {}), **package.get("devDependencies", {})}


@pytest.mark.parametrize("path", LAYOUT)
def test_monorepo_layout_exists(path: str) -> None:
    assert (ROOT / path).is_dir(), f"{path} is missing from the monorepo layout (P0-01 step 1)"


def test_every_python_package_has_at_least_one_test() -> None:
    for member in _workspace_members():
        tests = [
            p
            for p in (member / "tests").glob("test_*.py")
            if "def test_" in p.read_text(encoding="utf-8")
        ]
        assert tests, f"{member.relative_to(ROOT)} has no tests"


def test_web_app_has_at_least_one_unit_test() -> None:
    assert list((ROOT / "apps/web/tests/unit").glob("*.spec.ts"))


def test_python_dependencies_are_pinned_exactly() -> None:
    loose = [f"{p.relative_to(ROOT)}: {req}" for p, req in _python_requirements() if "==" not in req]
    assert not loose, f"unpinned Python dependencies: {loose}"


def test_npm_dependencies_are_pinned_exactly() -> None:
    loose = {name: v for name, v in _npm_dependencies().items() if not EXACT_NPM_VERSION.match(v)}
    assert not loose, f"unpinned npm dependencies: {loose}"


def test_lockfiles_are_committed() -> None:
    assert (ROOT / "uv.lock").is_file()
    assert (ROOT / "package-lock.json").is_file()


def test_every_direct_dependency_has_a_recorded_license() -> None:
    licenses = (ROOT / "docs/adr/licenses.md").read_text(encoding="utf-8")
    rows = {
        (cells[1].strip("` ").lower(), cells[2].strip("` "))
        for line in licenses.splitlines()
        if line.startswith("|") and len(cells := line.split("|")) > 4
    }
    expected = {
        (re.split(r"[\[=]", req, maxsplit=1)[0].lower(), req.split("==")[1])
        for _, req in _python_requirements()
    } | {(name.lower(), version) for name, version in _npm_dependencies().items()}

    missing = sorted(f"{name}=={version}" for name, version in expected - rows)
    assert not missing, f"add these to docs/adr/licenses.md: {missing}"


def test_container_images_are_pinned() -> None:
    sources = [ROOT / "docker-compose.yml", *ROOT.glob("apps/*/Dockerfile")]
    images: list[str] = []
    for source in sources:
        text = source.read_text(encoding="utf-8")
        images += re.findall(r"^\s*image:\s*(\S+)", text, flags=re.MULTILINE)
        images += re.findall(r"^FROM\s+(?:--\S+\s+)?(\S+)", text, flags=re.MULTILINE)
        images += re.findall(r"^COPY\s+--from=(\S+:\S+)", text, flags=re.MULTILINE)
    assert images
    for image in images:
        tag = image.rsplit(":", 1)[-1] if ":" in image else ""
        assert tag, f"{image} has no tag"
        assert tag != "latest", f"{image} uses latest"
        assert re.search(r"\d", tag), f"{image} is not pinned to a version"


def test_compose_defines_the_local_stack() -> None:
    compose = (ROOT / "docker-compose.yml").read_text(encoding="utf-8")
    for service in COMPOSE_SERVICES:
        assert re.search(rf"^  {service}:\s*$", compose, flags=re.MULTILINE), service
    assert re.search(r"image:\s*postgres:16\.", compose)


def test_makefile_has_the_standard_targets() -> None:
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    for target in MAKE_TARGETS:
        assert re.search(rf"^{target}:", makefile, flags=re.MULTILINE), target


def test_pull_request_template_has_the_traceability_table() -> None:
    template = (ROOT / ".github/pull_request_template.md").read_text(encoding="utf-8")

    assert "| Task | PRD section | Requirement ID | Test name |" in template


def test_codeowners_routes_engines_to_the_or_specialist() -> None:
    codeowners = (ROOT / ".github/CODEOWNERS").read_text(encoding="utf-8")
    engine_rules = [
        line for line in codeowners.splitlines() if line.startswith("/packages/engines/")
    ]

    assert engine_rules
    assert "or-specialist" in engine_rules[0]


def test_agent_instructions_are_at_the_repository_root() -> None:
    assert (ROOT / "CLAUDE.md").is_file()
    assert (ROOT / "AGENTS.md").is_file()
