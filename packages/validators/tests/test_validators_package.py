import importlib


def test_validators_package_imports_and_exposes_no_validator_yet() -> None:
    module = importlib.import_module("nasq_validators")

    assert module.__all__ == []
