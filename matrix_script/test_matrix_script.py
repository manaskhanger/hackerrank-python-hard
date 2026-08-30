"""Public sample and extra decode cases for Matrix Script."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "matrix_script.py"


def run_script(stdin: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=stdin,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.rstrip("\n")


def test_source_avoids_if_token():
    tokens = SCRIPT.read_text().replace("\n", " ").split()
    assert "if" not in tokens


def test_official_sample():
    sample = Path(__file__).with_name("sample_input.txt").read_text()
    # Column read: This$#is% Matrix#  %!
    # Symbols between letters become one space; trailing "#  %!" is kept.
    assert run_script(sample) == "This is Matrix#  %!"


def test_plain_letters_unchanged():
    stdin = "2 2\nAB\nCD\n"
    # columns: A C, B D -> ACBD
    assert run_script(stdin) == "ACBD"


def test_symbols_between_letters_become_one_space():
    stdin = "2 3\nA#B\nx!y\n"
    # columns: A x, # !, B y -> Ax#!By -> Ax By
    assert run_script(stdin) == "Ax By"


def test_leading_and_trailing_symbols_kept():
    stdin = "1 5\n#A$B!\n"
    assert run_script(stdin) == "#A B!"


def test_spaces_in_grid_are_symbols():
    stdin = "2 3\nA B\nC D\n"
    # A C, [space][space], B D -> AC  BD -> AC BD
    assert run_script(stdin) == "AC BD"
