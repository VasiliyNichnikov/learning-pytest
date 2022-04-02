"""
1) PyTest не ограничивает список фикстур вызываемые для тесты.
2) Так же любая фикстура может вызывать к исполнению любое количество фикстур для себя.
"""

import pytest


@pytest.fixture()
def fixture1(request):
    print("Fixture 1")


@pytest.fixture()
def fixture2(request):
    print("Fixture 2")


@pytest.fixture()
def fixture3(request, fixture2):
    print("Fixture 3")


def test_with_two_fixtures(fixture1, fixture2):
    print("Test with two fixtures")


def test_with_one_fixture(fixture3):
    print("Test with one fixture")