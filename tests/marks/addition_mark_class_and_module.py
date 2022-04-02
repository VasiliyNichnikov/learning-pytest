"""
    Также меткой можно пометить не только тест, но и класс, модуль
    (задается через изменение импортируемого модуля) или его запуска, получаемый через
    параметризацию.
"""

import pytest

pytest_mark = pytest.mark.level1

def test_1():
    print("Test 1")

@pytest.mark.level2
class TestClass:
    def test_2(self):
        print("Test 2")

    @pytest.mark.level3
    def test(self):
        print("Test 3")