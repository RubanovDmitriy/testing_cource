"""Trying to figure out fixtures and scopes"""


def test_function_fixture_sum(function_fixture):
    assert sum(function_fixture) == 3


def test_function_fixture_type(function_fixture):
    assert isinstance(function_fixture, tuple)


def test_module_fixture_type(module_fixture):
    assert isinstance(module_fixture, list)


def test_module_fixture_len(module_fixture):
    assert len(module_fixture) == 10


def test_module_fixture_sum(module_fixture):
    assert sum(module_fixture) == 55


def test_session_fixture_len(session_fixture):
    assert len(session_fixture) == 3


def test_session_fixture_type(session_fixture):
    assert isinstance(session_fixture, dict)


class TestClass:
    """Trying class fixtures"""

    def test_class_fixture_len(self, class_fixture):
        assert len(class_fixture) == 27

    def test_class_fixture_split(self, class_fixture):
        assert class_fixture.split() == ['Hello,', 'I', 'am', 'string', 'for', 'test']

    def test_sum_fixtures(self, class_fixture, module_fixture):
        assert class_fixture.split() + module_fixture == [
            'Hello,', 'I', 'am', 'string', 'for', 'test', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]
