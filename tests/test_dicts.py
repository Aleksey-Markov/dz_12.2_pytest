import pytest
from pytest_proj.utils.dicts import get_val


@pytest.fixture()
def dictionary():
    return {1: 'first', 2: 'second'}


def test_get_val(dictionary):
    assert get_val(dictionary, 1) == 'first'
    assert get_val(dictionary, 2) == 'second'


def test_get_val_empty_dict():
    assert get_val({}, 1) == 'git'
    assert get_val({}, 2, 'python') == 'python'


def test_get_val_wrong_key(dictionary):
    assert get_val(dictionary, 3) == 'git'
    assert get_val(dictionary, 'git', 'python') == 'python'
