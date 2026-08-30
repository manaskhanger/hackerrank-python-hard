# Validating Postal Codes

HackerRank: https://www.hackerrank.com/challenges/validating-postalcode/problem  
Slug: `validating-postalcode` · Subdomain: Regex and Parsing · Difficulty: Hard

## Restatement

A 6-digit postal string is valid only when **both** hold:

1. It is an integer from 100000 through 999999 (no leading zeros).
2. It has **at most one** alternating repetitive digit pair: a digit that repeats with exactly one character between the two copies (`aba` style). Overlapping pairs all count.

HackerRank already supplies the check. You only fill in two patterns:

- `regex_integer_in_range` — whole-string match for that numeric range
- `regex_alternating_repetitive_digit_pair` — one match per overlapping pair (lookahead so neighbours both count)

The site awards 0 for using a standalone `if` token, so this file avoids that word.

## Run

```bash
echo 110000 | python3 validating_postal_codes.py
python3 -m pytest test_validating_postal_codes.py -q
```

On HackerRank, paste the two `regex_*` assignments. The I/O stub is locked in the editor; this file includes the same stub so local stdin/stdout works.
