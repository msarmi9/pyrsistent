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
        for odd in (True, False):
            pal = expanded_palindrome(s, center, odd=odd)
            if len(pal) > len(longest):
                longest = pal
            elif len(pal) == len(longest):
                longest = min(pal, longest)
    return longest


def expanded_palindrome(s: str, center: int, odd: bool) -> str:
    """Return the longest odd or even length palindrome centered at a given index."""
    l = center - 1
    r = center + 1 if odd else center
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
