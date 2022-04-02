import pytest
from pytest import FixtureRequest


@pytest.fixture(scope="function")
def resource_setup(request: FixtureRequest):
    print(f"Fixture name: {request.fixturename}")
    print(f"Scope: {request.scope}")
    print(f"Function name: {request.function.__name__}")
    print(f"Request cls: {request.cls}")
    print(f"Request module name: {request.module.__name__}")
    print(f"Request path: {request.path}")


def test_1(resource_setup):
    assert True


class TestClass(object):
    def test_2(self, resource_setup):
        assert True