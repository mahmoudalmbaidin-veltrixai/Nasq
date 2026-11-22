import importlib


def test_inventory_engine_package_imports_and_exposes_no_engine_yet() -> None:
    module = importlib.import_module("nasq_engine_inventory")

    assert module.__all__ == []
