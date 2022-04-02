"""
    Фикстуры можно описывать в файле conftest.py, который
    автоматически импортируется PyTest. При этом фикстура может иметь любой уровень
    (Только через описание в этом файле можно создать фикстуру с уровнем "Сессия")
    *Примечание: модули должны начинаться с ключевого слова "test"
"""

import pytest
from pytest import FixtureRequest


@pytest.fixture(scope="session", autouse=True)
def auto_session_resource(request: FixtureRequest):
    """
    Auto session resource fixture
    :param request:
    :return:
    """
    print("Auto session resource")

    def auto_session_resource_teardown():
        print("Auto session resource teardown")

    request.addfinalizer(auto_session_resource_teardown)


@pytest.fixture(scope="session")
def manually_session_resource(request: FixtureRequest):
    """Manual set session resource fixture"""
    print("Manually session resource setup")

    def manually_session_resource_teardown():
        print("Manually session resource teardown")

    request.addfinalizer(manually_session_resource_teardown)


@pytest.fixture(scope="function")
def function_resource(request: FixtureRequest):
    """Fixture resource fixture"""
    print("Function resource setup")

    def function_resource_teardown():
        print("Function resource teardown")

    request.addfinalizer(function_resource_teardown)

