"""
Digit Anagrams

Given an array of ints, count the number of pairs of digit anagrams. Two ints are considered digit
anagrams if they contain the same digits, i.e. one int can be obtained from the other by
rearranging its digits.

For example, 827 and 278 are digit anagrams but 550 and 500 are not.
"""

from collections import namedtuple

import pytest


def count_anagrams(nums: list[int]) -> int:
    """Return the number of pairs of digit anagrams in `nums`."""
    total, ana2count = 0, {}
    for num in nums:
        freqs = tuple(encode(num))
        total += ana2count.get(freqs, 0)
        ana2count[freqs] = ana2count.setdefault(freqs, 0) + 1
    return total


def encode(num: int) -> list[int]:
    """Encode `num` as a list whose i-th entry is the frequency of i in `num`."""
    freqs = [0] * 10
    while num > 0:
        digit = num % 10
        freqs[digit] += 1
        num = (num - digit) // 10
    return freqs


class TestCountAnagrams:
    """Tests `count_anagrams` on various anagram scenarios."""

    Example = namedtuple("Example", ["input", "expected"])

    examples = [
        Example([25, 35, 872, 228, 53, 278, 872], 4),
        Example([550, 50, 505, 5, 500], 1),
        Example([123, 123, 123], 3),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_when_anagrams_(self, example):
        got = count_anagrams(example.input)
        assert got == example.expected
