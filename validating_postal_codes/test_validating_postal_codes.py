"""Public sample, statement examples, and range-edge cases."""

import re
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent / "validating_postal_codes.py"


def load_regexes():
    namespace = {}
    for line in SCRIPT.read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith("regex_"):
            exec(stripped, namespace)
    return (
        namespace["regex_integer_in_range"],
        namespace["regex_alternating_repetitive_digit_pair"],
    )


RANGE_RE, PAIR_RE = load_regexes()


def stub_result(code: str) -> bool:
    return bool(re.match(RANGE_RE, code)) and len(re.findall(PAIR_RE, code)) < 2


def run_script(stdin: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=stdin,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


def test_loaded_regexes_are_the_intended_patterns():
    assert RANGE_RE == r"^[1-9][0-9]{5}$"
    assert PAIR_RE == r"(\d)(?=\d\1)"


def test_official_sample_110000_is_false():
    # Two overlapping 0-pairs in 110000.
    assert run_script("110000\n") == "False"
    assert stub_result("110000") is False


@pytest.mark.parametrize(
    "code, expected",
    [
        ("121426", True),   # one 1-pair, from the statement
        ("523563", True),   # no pairs, from the statement
        ("552523", False),  # 5-pair and 2-pair, from the statement
        ("123456", True),
        ("100000", False),  # several 0-pairs
        ("101010", False),  # several 1/0 pairs
        ("123454", True),   # single 4-pair at the end
        ("999999", False),  # many 9-pairs
        ("100001", False),  # three overlapping 0-pairs
        ("121456", True),   # a single 1-pair
    ],
)
def test_statement_and_hand_cases(code, expected):
    assert stub_result(code) is expected
    assert run_script(code + "\n") == str(expected)


@pytest.mark.parametrize(
    "code",
    ["099999", "10000", "1000000", "abcdef", "12345a"],
)
def test_out_of_range_rejected(code):
    assert stub_result(code) is False
    assert run_script(code + "\n") == "False"


def test_empty_input_is_out_of_range():
    assert stub_result("") is False
