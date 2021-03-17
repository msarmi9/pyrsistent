"""
Max Palindrome

Given a string, find the longest palindrome that can be made from its characters. If more than one
such palindrome exists, return the lexicographically smallest one.
"""

from collections import namedtuple
from collections import Counter

import pytest


def max_palindrome(s: str) -> str:
    """Return the lexicographically smallest longest palindrome made up of a string's chars."""
    counts = Counter(s)
    half, middle = "", ""
    for char, count in sorted(counts.items()):
        half += char * (count // 2)
        if not middle and count % 2 == 1:
            middle = char
    return half + middle + half[::-1]


class TestMaxPalindrome:

    Example = namedtuple("Example", ["input", "answer"])

    examples = [
        Example("aa", "aa"),
        Example("aaa", "aaa"),
        Example("aaab", "aaa"),
        Example("aaaab", "aabaa"),
        Example("aaabbbcc", "abcacba"),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_max_palindrome(self, example):
        got = max_palindrome(example.input)
        assert got == example.answer
