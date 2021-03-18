"""
Longest Palindromic Substring

Given a string, return its lexicographically smallest longest palindromic substring(s).
"""

from collections import namedtuple

import pytest


def longest_palindromic_substr(s: str) -> str:
    """Return the lexicographically smallest longest palindromic substring."""
    longest = ""
    for center in range(len(s)):
        for offset in (0, 1):
            substr = expand_palindrome(s, center, center + offset)
            if len(substr) > len(longest):
                longest = substr
            elif len(substr) == len(longest):
                longest = min(substr, longest)
    return longest


def expand_palindrome(s: str, l: int, r: bool) -> str:
    """Return the longest palindrome centered at the substring s[l:r]."""
    while 0 <= l and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1: r]


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
