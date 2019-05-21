from src.scanners import ParamScanners as ps
# import pytest


def test_get_project():
    query = "this is a #test"
    assert 'test' == ps.get_project(query)

