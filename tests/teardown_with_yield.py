"""
    Использование в фиксаторе для вызова teardown конструкцию yield
    Так же важно помнить, что в таком случае нужно писать @pytes.yield_fixture() вместо @pytest.fixture()
"""

import pytest


@pytest.yield_fixture()
def resource_setup():
    print("Resource setup")
    yield
    print("Resource teardown")


def test_1_that_need_resources(resource_setup):
    print("Test 1 that need resources")


def test_2_that_does_not():
    print("Test 2 that doesn't")


def test_3_that_does_again(resource_setup):
    print("Test 3 that does again")
