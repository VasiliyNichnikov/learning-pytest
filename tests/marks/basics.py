"""
    PyTest поддерживает класс декораторов @pytest.mark называемый "меткасми"(marks). Базовый список
    включает в себя следующие метки:

    1) @pytest.mark.parametrize - для параметризации тестов.
    2) @pytest.mark.xfail - помечает, что тест должен не проходить и PyTest будет воспринимать это,
    как ожидаемое поведение. (Полезно как временная метка на разрабатываемые функции). Также эта метка
    может принимать условие, при котором тест будет помечаться данной меткой.
    3) @pytest.mark.skipif - позволяет задать условие при выполнении которого тест будет пропущен.
    4) @pytest.mark.usefixtures - позволяет перечислить все фикстуры, вызываемые для теста.
"""

import sys

import pytest


@pytest.mark.xfail()
def test_failed():
    assert False


@pytest.mark.xfail(sys.platform != "win64", reason="requires windows 64bit")
def test_failed_for_not_win32_systems():
    assert False


@pytest.mark.skipif(sys.platform != "win64", reason="requires windows 64bit")
def test_skipped_for_not_win64_systems():
    assert False
