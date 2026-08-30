"""Maximize It! — stdin/stdout solution for HackerRank (Python 3)."""

from itertools import product


def max_square_sum_mod(lists, modulus):
    """Pick one integer from each list to maximise (sum of squares) % modulus."""
    return max(sum(item * item for item in pick) % modulus for pick in product(*lists))


def solve_from_lines(lines):
    k, modulus = map(int, lines[0].split())
    lists = []
    for row in lines[1 : 1 + k]:
        values = list(map(int, row.split()))
        lists.append(values[1:])
    return max_square_sum_mod(lists, modulus)


def main():
    import sys

    lines = sys.stdin.read().splitlines()
    print(solve_from_lines(lines))


if __name__ == "__main__":
    main()
