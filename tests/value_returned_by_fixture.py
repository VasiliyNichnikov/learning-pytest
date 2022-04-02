"""
    Демонстрация того, что фикстур может возвращать значения
"""

import pytest
from pytest import FixtureRequest


@pytest.fixture(scope="function")
def resource_setup(request: FixtureRequest):
    print("\nConnect to db")
    db = {"Red": 0, "Green": 1, "Blue": 2}

    def resource_teardown():
        print("\nDisconnect")

    request.addfinalizer(resource_teardown)
    return db


def test_db(resource_setup):
    for k in resource_setup.keys():
        print(f"Color {k}, {resource_setup[k]}")


def test_red(resource_setup):
    assert resource_setup["Red"] == 0


def test_blue(resource_setup):
    assert resource_setup["Blue"] == 2
