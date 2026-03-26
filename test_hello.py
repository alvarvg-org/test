from hello import hello


def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
