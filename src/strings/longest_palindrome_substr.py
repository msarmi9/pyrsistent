"""
Longest Palindromic Substring

Given a string, return its lexicographically smallest longest palindromic substring(s).
"""

from collections import namedtuple
from typing import Optional

import pytest


def longest_palindromic_substr(s: str) -> str:
    """Return the lexicographically smallest longest palindromic substring."""
    longest = ""
    for center in range(len(s)):
        for odd in (True, False):
            l, r = is_palindrome(s, center, odd=odd)
            substr = s[l:r]
            if len(substr) > len(longest):
                longest = substr
            elif len(substr) == len(longest):
                longest = min(substr, longest)
    return longest


def is_palindrome(s: str, center: int, odd: bool) -> (int, int):
    """Check if a char is the center of an odd or even length palindrome and return its bounds."""
    l = center - 1 if odd else center
    r = center + 1
    while 0 <= l < r < len(s):
        if s[l] != s[r]:
            return l + 1, r
        l -= 1
        r += 1
    return l + 1, r


def longest_palindromic_substr_naive(s: str) -> str:
    """Return the lexicographically smallest longest palindromic substring."""
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j]
            if substr == substr[::-1]:
                if len(substr) > len(longest):
                    longest = substr
                elif len(substr) == len(longest):
                    longest = min(substr, longest)
    return longest


class TestPalindromicSubstring:

    Example = namedtuple("Example", ["input", "answer"])

    examples = [
        Example("babad", "aba"),
        Example("abc", "a"),
        Example("cbbd", "bb"),
        Example("aaa", "aaa"),
        Example("aaaa", "aaaa"),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_longest_palindromic_substr(self, example):
        got = longest_palindromic_substr(example.input)
        assert got == example.answer
