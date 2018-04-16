import pytest


def test_method_a(fixture_yield_example):
    print("running test in method a")


def test_method_b(fixture_module_example):
    print("running test in method b")

def test_method_c(fixture_module_example, fixture_yield_example):
    print("running test in method c")