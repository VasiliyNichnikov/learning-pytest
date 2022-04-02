"""
    1) Второй вариант как можно добавить фиксатор к функции.
    Через @pytest.mark.usefixtures("resource_setup")
    2) Добавление фиксатора, который включается для всех тестовых функций, с помощью параметра autouse
    Так же указывается параметр scope:
        function – фикстура запускается для каждого теста
        cls – фикстура запускается для каждого класса
        module – фикстура запускается для каждого модуля
        session – фикстура запускается для каждой сессии (то есть фактически один раз)
"""


import pytest
from pytest import FixtureRequest


@pytest.fixture()
def resource_setup(request: FixtureRequest):
    print("Resource setup")

    def resource_teardown():
        print("Resource teardown")

    request.addfinalizer(resource_teardown)


@pytest.fixture(scope="function", autouse=True)
def another_resource_setup_with_autouse(request: FixtureRequest):
    print("Another resource setup with autouse")

    def resource_teardown():
        print("Another resource teardown with autouse")

    request.addfinalizer(resource_teardown)


def test_1_that_need_resources(resource_setup):
    print("Test 1 that need resources")


def test_2_that_does_not():
    print("Test 2 that doesn't")


@pytest.mark.usefixtures("resource_setup")
def test_3_that_does_again():
    print("Test 3 that does again")
