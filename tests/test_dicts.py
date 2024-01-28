import pytest
from pytest_proj.utils.dicts import get_val


def test_get_val():
    assert get_val({1: 'first', 2: 'second'}, 1) == 'first'
    assert get_val({1: 'first', 2: 'second'}, 2) == 'second'


def test_get_val_empty_dict():
    assert get_val({}, 1) == 'git'
    assert get_val({}, 2, 'python') == 'python'


def test_get_val_wrong_key():
    assert get_val({1: 'first', 2: 'second'}, 3) == 'git'
    assert get_val({1: 'first', 2: 'second'}, 'git', 'python') == 'python'
