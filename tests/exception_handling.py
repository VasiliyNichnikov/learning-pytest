"""
    PyTest также позволяет проверять корректность возвращаемых исключений при помощи "with pytest.raises()"
"""
import pytest


def function():
    print(1 / 0)


def test_exception():
    with pytest.raises(ZeroDivisionError):
        function()
