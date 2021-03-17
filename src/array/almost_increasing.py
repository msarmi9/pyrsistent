"""
Almost Increasing Sequence

Given an array of ints, determine if the array can be made strictly increasing by removing at most
1 element. For example, given [1, 2, 4, 3], we can remove 4 or 3, and given [5, 6, 7], we don't
have to remove anything.
"""

import pytest


def is_almost_increasing(seq: list[int]) -> bool:
    """Return True if a list can be made strictly increasing by removing at most 1 element."""
    i = first_non_increasing_pair(seq)
    if i == -1:
        return True
    if first_non_increasing_pair(seq[i-1: i] + seq[i+1:]) == -1:
        return True
    if first_non_increasing_pair(seq[i: i+1] + seq[i+2:]) == -1:
        return True
    return False


def first_non_increasing_pair(seq: list[int]) -> int:
    """Return the index of the first non-increasing pair of elements."""
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            return i
    return -1


class TestIsAlmostIncreasing:

    examples = [
        ([10, 1, 2, 3, 4], True),
        ([1, 2, 4, 3, 5], True),
        ([1, 2, 1, 2], False),
        ([8, 9, 1, 10, 2], False),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_is_almost_increasing(self, example):
        got = is_almost_increasing(example[0])
        assert got == example[1]
