"""
    Параметризация - это способ запустить один и тот же тест с разным набором входных параметров.
    Например, у нас есть функция, которая добавляет знак вопросв к строке, если она длинее 5 символов,
    восклицательный знак - менее 5 символов и точку, если в строке ровно 5 символов. Соответственно вместо
    того, чтобы писать три теста. мы можем написать один, но вызываемый с разными параметрами.

    Первый способ передачи параметров:
    Через значение параметра params фикстуры, в который можно передать массив значений.
    То есть фактически фикстура в данном случае представляет собой обертку, передающую параметры.
    А в сам тест они передаются через атрибут param объекта request.
"""
import pytest


def strange_string_function(string):
    if len(string) > 5:
        return string + "?"
    elif len(string) < 5:
        return string + "!"
    else:
        return string + "."


@pytest.fixture(scope="function", params=[
    ("abcdefg", "abcdefg?"),
    ("abc", "abc!"),
    ("abcde", "abcde.")
], ids=["len > 5", "len < 5", "len == 5"])  # Благодаря ids можно уточнить для каждого параметра,
# за что он отвечает и что тестирует
def parameter_test(request):
    return request.param


def test_strange_string_function(parameter_test):
    input_, expected_output = parameter_test
    result = strange_string_function(input_)
    print(f"Input: {input_}, output: {result}, expected: {expected_output}")
    assert result == expected_output
