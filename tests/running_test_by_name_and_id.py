"""
    Отдельные тесты из модулей можно запускать перечисляя полный путь к ним в виде
    module.py::class::method или module.py::function
    А также передавая с флагом -k часть их имени.

    Так например можно вызвать test_two следующем образом:
    pytest -s -v tests/running_test_by_name_and_id.py::test_two

    А так же с помощью ключа -k вызвать те тесты, которые содержат в название слово "one":
    pytest -s -v -k "one" tests/running_test_by_name_and_id.py
"""


def test_one():
    print("Test one")


def test_one_negative():
    print("Test one negative")


def test_two():
    print("Test two")
