from mock import Mock
from oops import logs


def test_color():
    assert logs.color('red', Mock(no_colors=False)) == 'red'
    assert logs.color('red', Mock(no_colors=True)) == ''
