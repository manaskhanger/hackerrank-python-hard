# Maximize It!

HackerRank: https://www.hackerrank.com/challenges/maximize-it/problem  
Slug: `maximize-it` · Subdomain: Itertools · Difficulty: Hard

## Restatement

You get `K` lists and a modulus `M`. Choose exactly one number from each list. Square those `K` numbers, add the squares, then take the result modulo `M`. Print the largest value that choice can produce.

Constraints are small (`K` and each list length at most 7), so enumerating the cartesian product is enough. Squares of values up to `10^9` fit in Python integers.

## Run

```bash
python3 maximize_it.py < sample_input.txt
python3 -m pytest test_maximize_it.py -q
```

Paste `maximize_it.py` into the HackerRank editor as Python 3.
