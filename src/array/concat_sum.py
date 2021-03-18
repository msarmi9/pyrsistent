"""
Concat Sum

Given an array of positive integers, find the sum of all concatenated pairs of entries. For
example, given a = [10, 2], we have:

    * a[0] concat a[0] = 1010
    * a[0] concat a[1] = 102
    * a[1] concat a[0] = 210
    * a[2] concat a[2] = 22

which sum to 1010 + 102 + 210 + 22 = 1344.
"""

from collections import namedtuple

import pytest


def concat_sum(arr: list[int]) -> int:
    """Return the sum of all concatenated pairs of elements."""
    # An element can be on the right (1s place) or the left (offset by len(other))
    el_sum, offset_sum = 0, 0
    for el in arr:
        el_sum += el
        offset_sum += 10 ** len(str(el))
    return len(arr) * el_sum + offset_sum * el_sum


def concat_sum_naive(arr: list[int]) -> int:
    """Return the sum of all concatenated pairs of entries."""
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            total += int(str(arr[i]) + str(arr[j]))
    return total


class TestConcatSum:

    Example = namedtuple("example", ["input", "expected"])

    examples = [
        Example([10, 2], 1344),
        Example([1, 2, 3], 198),
        Example([4, 5, 10], 2337),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_concat_sum(self, example):
        got = concat_sum(example.input)
        assert got == example.expected
