def test_package_imports():
    import nids

    assert nids.__name__ == "nids"


def test_core_dependencies_import():
    import numpy  # noqa: F401
    import pandas  # noqa: F401
    import sklearn  # noqa: F401
