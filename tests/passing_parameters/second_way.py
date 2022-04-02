"""
    Это второй способ как можно передавать параметры
    Второй способ имеет одно преимущество: если указать несколько меток с разными параметрами,
    то в итоге тест будет запущен со всеми возможными наборами параметров (то есть декартово произведение параметров)
"""

import pytest


def id_function_x(value):
    return f"x=({value})"


def id_function_y(value):
    return f"y=({value})"


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 11])
def test_cross_parameters(x, y):
    print(f"x: {x}, y: {y}")
    assert True


@pytest.mark.parametrize("x", [5, 3], ids=id_function_x)
@pytest.mark.parametrize("y", [2, 1], ids=id_function_y)
def test_cross_parameters(x, y):
    print(f"x: {x}, y: {y}")
    assert True


@pytest.mark.parametrize("x", [-1, 2], ids=["negative x", "position y"])
def test_x_parameter(x):
    print(f"x: {x}")
    assert True
