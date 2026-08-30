"""Matrix Script — stdin/stdout solution for HackerRank (Python 3).

Avoids a standalone "if" token because the custom checker zeros the score
when that word appears as its own split token.
"""

import re
import sys

raw_lines = sys.stdin.read().splitlines()
n, m = map(int, raw_lines[0].split())
rows = raw_lines[1 : 1 + n]
decoded = "".join("".join(column) for column in zip(*rows))
print(re.sub(r"(?<=[0-9A-Za-z])[^0-9A-Za-z]+(?=[0-9A-Za-z])", " ", decoded))
