import importlib


def test_contracts_package_imports_and_exports_nothing_before_p0_04() -> None:
    module = importlib.import_module("nasq_contracts")

    assert module.__all__ == []
