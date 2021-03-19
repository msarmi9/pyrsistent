"""
Number of Subsequence Occurences

Given two strings, count the number of times one appears as a subsequence of the other. For
example, given s="rabbbit" and t="rabbit", t appears as a subsequence of s 3 times.
"""

from collections import defaultdict
from collections import namedtuple

import pytest


# Moral: Count how many times each char of `t` is seen in its correct sequential position in `s`
# How? By iterating and summing the times we've seen the previous char in its correct position
def count_subseqs(string: str, target: str) -> int:
    """Count the number of times `target` appears as a subsequence of a string."""
    seen = [1] + [0] * len(target)
    char2ix = defaultdict(list)
    for i, c in enumerate(target):
        char2ix[c].append(i)
    for c in string:
        for i in reversed(char2ix[c]):
            seen[i + 1] += seen[i]
    return seen[-1]


#        "" a  ba aba
#  ""    1  0  0  0
#     a  1  1  0  0
#    ba  1  1  1  0
#   bba  1  1  2  0
#  abba  1  2  2  2

def count_subseqs2(s: str, t: str) -> int:
    """Count the number of times `t` appears as a subsequence of a string."""
    n, m = len(s), len(t)
    seen = [[1] + [0] * m for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[-i] == t[-j]:
                seen[i][j] += seen[i - 1][j - 1]
            seen[i][j] += seen[i - 1][j]
    return seen[-1][-1]


# O(n!m!)
def count_subseqs_recurse(s: str, t: str) -> int:
    """Recursively count the number of times `t` appears as a subsequence of a s."""
    if not t: return 1
    if not s: return 0
    if s[0] != t[0]:
        return count_subseqs_recurse(s[1:], t)
    return count_subseqs_recurse(s[1:], t) + count_subseqs_recurse(s[1:], t[1:])


class TestCountSubseqs:

    Example = namedtuple("Example", ["input", "expected"])

    examples = [
        Example(("abba", "aba"), 2),
        Example(("rabbbit", "rabbit"), 3),
        Example(("babgbag", "bag"), 5),
        Example(("rollinrollin", "roll"), 8),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_count_subseqs(self, example):
        got = count_subseqs(*example.input)
        got2 = count_subseqs2(*example.input)
        assert got == got2 == example.expected
