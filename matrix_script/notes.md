# Matrix Script

HackerRank: https://www.hackerrank.com/challenges/matrix-script/problem  
Slug: `matrix-script` · Subdomain: Regex and Parsing · Difficulty: Hard

## Restatement

You are given an `N` by `M` character grid. Read it **column by column** (top to bottom, left to right) to form one long string.

Then collapse every run of non-alphanumeric characters that sits **between two alphanumeric characters** into a single space. Leading or trailing symbol runs stay as they are.

Alphanumeric here means `[A-Za-z0-9]` only (underscore is not alphanumeric).

The custom checker awards 0 if the source contains `if` as its own token, so the solution uses `zip` plus one substitution and no `if`.

## Run

```bash
python3 matrix_script.py < sample_input.txt
python3 -m pytest test_matrix_script.py -q
```

Paste `matrix_script.py` into the HackerRank editor as Python 3.
