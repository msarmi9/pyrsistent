"""
Number of Subsequence Occurences

Given two strings, count the number of times one appears as a subsequence of the other. For
example, given s="rabbbit" and t="rabbit", t appears as a subsequence of s 3 times.
"""

from collections import defaultdict
from collections import namedtuple

import pytest


# Moral: Count how many times each char of `t` is seen in its correct sequential position in `s`
# How? By iterating and summing the times we've seen the prior char in its correct position
def count_subsequences(string: str, target: str) -> int:
    """Count the number of times `target` appears as a subsequence of a string."""
    char2ix = defaultdict(list)
    seen = [1] + [0] * len(target)
    for i, c in enumerate(target):
        char2ix[c].append(i)
    for c in string:
        for i in reversed(char2ix[c]):
            seen[i + 1] += seen[i]
    return seen[-1]


class TestCountSubsequences:

    Example = namedtuple("Example", ["input", "expected"])

    examples = [
        Example(("rabbbit", "rabbit"), 3),
        Example(("babgbag", "bag"), 5),
        Example(("rollinrollin", "roll"), 8),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_count_subsequences(self, example):
        got = count_subsequences(*example.input)
        assert got == example.expected
