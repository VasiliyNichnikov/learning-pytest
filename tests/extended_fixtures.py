"""
    Вызов setup и teardown конкретно в fixture
    И подключение fixture к функциям тестирования

    Так же указывается параметр scope:
        function – фикстура запускается для каждого теста (выставлена по умолчанию)
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

    request.addfinalizer(resource_teardown)  # Добавляем resource_teardown конкретно для данной фикстуры, чтобы метод вызвался как teardown


def test_1_that_need_resources(resource_setup):
    print("Test 1 that need resources")


def test_2_that_does_not():
    print("Test 2 that doesn't")


def test_3_that_does_again(resource_setup):
    print("Test 3 that does again")
