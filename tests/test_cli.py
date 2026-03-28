import pytest
from iceman.cli import main


def test_run(capsys):
    import sys
    sys.argv = ["iceman", "run"]
    assert main() == 0
    captured = capsys.readouterr()
    assert "running" in captured.out.lower()
