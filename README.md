# HackerRank Python (Hard)

Original Python 3 solutions for every challenge currently marked **Hard** in HackerRank's [Python domain](https://www.hackerrank.com/domains/python?filters%5Bdifficulty%5D%5B%5D=hard).

The official track (as of 31 Aug 2026) lists **three** Hard problems. Easy/Medium challenges are not included.

## Problems

| Title | Slug | Subdomain | URL |
| --- | --- | --- | --- |
| Maximize It! | `maximize-it` | Itertools | https://www.hackerrank.com/challenges/maximize-it/problem |
| Validating Postal Codes | `validating-postalcode` | Regex and Parsing | https://www.hackerrank.com/challenges/validating-postalcode/problem |
| Matrix Script | `matrix-script` | Regex and Parsing | https://www.hackerrank.com/challenges/matrix-script/problem |

Each folder has:

- a standalone `.py` script that reads stdin and writes stdout (pasteable into HackerRank)
- `notes.md` with a short original restatement and how to run
- `test_*.py` covering the public sample plus a few extra cases

## How to run tests

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -q
```

Run one problem:

```bash
python3 maximize_it/maximize_it.py < maximize_it/sample_input.txt
python3 -m pytest maximize_it/test_maximize_it.py -q
```

## Skipped

- **Company Logo** (`most-commons`) — HackerRank marks it **Medium**, not Hard.
