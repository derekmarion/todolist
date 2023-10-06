# Test todo.py

import somefile.py

# List function tests
def test_list_input(monkeypatch, capsys):
	monkeypatch.seattr('builtins.input', lambda_: "1")

    i = input("Beginning prompt:")
    assert i == 1

    out, err = capsys.readouterr()
    assert out == "Expected output"

