import pytest

# yield to run at the end of every method
@pytest.fixture()
def fixture_yield_example():
    print("This will run if inherited in the base class")
    yield
    print("statement runs at the end if inherited")


# if scope is defined as module, it runs for a module level
@pytest.fixture(scope='module')
def fixture_module_example():
    print("MODULE LEVEL FIXTURE")
    yield
    print("MODULE LEVEL TEARDOWN")

