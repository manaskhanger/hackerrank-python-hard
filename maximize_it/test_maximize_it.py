"""Sample and extra cases for Maximize It!"""

import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent / "maximize_it.py"
sys.path.insert(0, str(SCRIPT.parent))
from maximize_it import max_square_sum_mod, solve_from_lines  # noqa: E402


def run_script(stdin: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=stdin,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


def test_official_sample_via_stdin():
    sample = Path(__file__).with_name("sample_input.txt").read_text()
    assert run_script(sample) == "206"


def test_official_sample_via_solver():
    lines = [
        "3 1000",
        "2 5 4",
        "3 7 8 9",
        "5 5 7 8 9 10",
    ]
    # 5^2 + 9^2 + 10^2 = 206
    assert solve_from_lines(lines) == 206


def test_single_list_picks_best_residue():
    # 4^2 % 5 == 1, 3^2 % 5 == 4
    assert max_square_sum_mod([[3, 4]], 5) == 4


def test_modulo_beats_raw_largest_squares():
    # Largest numbers give 9^2 + 9^2 = 162 % 10 = 2, but 1 and 2 give 5.
    assert max_square_sum_mod([[9, 1], [9, 2]], 10) == 5


def test_large_elements_stay_in_python_ints():
    huge = 10**9
    assert max_square_sum_mod([[huge], [huge]], 1000) == (2 * huge * huge) % 1000


@pytest.mark.parametrize(
    "lists, modulus, expected",
    [
        ([[1]], 1, 0),
        ([[2, 3], [4]], 7, (4 + 16) % 7),  # 2^2 + 4^2
        ([[5], [7], [8]], 1000, 25 + 49 + 64),
    ],
)
def test_small_hand_cases(lists, modulus, expected):
    assert max_square_sum_mod(lists, modulus) == expected
