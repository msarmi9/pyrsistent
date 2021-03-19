"""
Count Distinct Subsequences

Given a string, count the number of distinct, non-empty subsequences. For example, "abc" has 7
distinct subsequences: a, b, c, ab, bc, ac, abc
"""

from collections import namedtuple

import pytest


# Moral: Iterate over `s` and count the number of distinct subequences up to that point
# How? The number of seqs doubles at each step (can add/omit ith char). Just need to rm duplicates
# The number of duplicates from a repeat char `c` == number of seqs right *before* we last saw `c`
def count_distinct_subseqs(s: str) -> int:
    """Return the number of distinct, non-empty subsequences of a string."""
    seen = {}
    counts = [1] + [0] * len(s)
    for i, c in enumerate(s):
        counts[i + 1] = 2 * counts[i]
        if lastix := seen.get(c):
            counts[i + 1] -= counts[lastix - 1]
        seen[c] = i + 1
    return counts[-1] - 1


class TestCountDistinctSubsequences:

    Example = namedtuple("Example", ["input", "expected"])

    examples = [
        Example("aaa", 3),
        Example("aba", 6),
        Example("abc", 7),
        Example("abba", 10),
        Example("abab", 11),
        Example("abcd", 15),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_count_distinct_subseqs(self, example):
        got = count_distinct_subseqs(example.input)
        assert got == example.expected
