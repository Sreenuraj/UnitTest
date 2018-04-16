'''
file name should start with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
-v verbose
'''


import pytest

# yield to run at the end


@pytest.yield_fixture()
def fixture_yield_example():
    print("This will run if inherited in the base class")
    yield
    print("statement runs at the end if inherited")


def test_method_a(fixture_yield_example):
    print("running test in method a")


def test_method_b():
    print("running test in method b")
