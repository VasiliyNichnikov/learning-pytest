"""
    Основной алгоритм работы различных setup и teardown
"""


def setup():
    print("Basic setup into module")


def teardown():
    print("Basic teardown into module")


def setup_module(module):
    print("Module setup")


def teardown_module(module):
    print("Module teardown")


def setup_function(function):
    print("Function setup")


def teardown_function(function):
    print("Function teardown")


def test_number_3_4():
    print("Test 3 * 4")
    assert 3 * 4 == 12


def test_strings_a_3():
    print("Test a * 3")
    assert 'a' * 3 == "aaa"
