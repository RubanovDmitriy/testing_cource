"""conftest file for fixtures and scopes"""
import pytest


@pytest.fixture(scope="function")
def function_fixture(request):
    """return tuple of numbers"""
    number_one = 1
    number_two = 2
    print(f"\n Hello from {request.scope} fixture!")
    return number_one, number_two


@pytest.fixture(scope="module")
def module_fixture(request):
    """return list of numbers"""
    list_for_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\n Hello from {request.scope} fixture!")
    return list_for_test


@pytest.fixture(scope="session")
def session_fixture(request):
    """return dict of strings"""
    dict_for_test = {
        1: 'a',
        2: 'b',
        3: 'c',
    }
    print(f"\n Hello from {request.scope} fixture!")
    return dict_for_test


@pytest.fixture(scope="class")
def class_fixture(request):
    """return string"""
    string_for_test = 'Hello, I am string for test'
    print(f"\n Hello from {request.scope} fixture!")
    return string_for_test
