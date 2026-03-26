from io import StringIO
import sys

from hello import hello


def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
