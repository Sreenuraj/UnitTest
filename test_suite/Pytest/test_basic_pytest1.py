'''
Naming conventions
File names should start or end with “test”, as in test_example.py or example_test.py
Class name should start with “Test”, as in TestExample
Test method names should start with “test_”, as in test_example
'''

import pytest

# Fixture to run at the start
@pytest.fixture()
def fixture_example():
    print("This will run if inherited in the base class")


def test_method_a(fixture_example):
    print("running test in method a")


def test_method_b():
    print("running test in method b")

