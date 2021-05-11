"""
Longest Subarray Check

Given two integer arrays A, B and an array C of distinct integers, determine if B is a longest
contiguous subarray of A made up of elements from C.

For example, given the arrays A=[1, 1, 5, 1, 2], B=[1, 2], and C=[2, 1], the longest contiguous
subarrays of A composed of elements from C are [1, 1] and B=[1, 2].
"""

from collections import namedtuple

import pytest


def is_longest_subarray(A: list[int], B: list[int], C: list[int]) -> bool:
    """Determine if B is a longest contiguous subarray of A composed of elements of C."""
    C = set(C)
    if len(B) > len(A) or any(b not in C for b in B):
        return False

    found_B = False
    matched_B, matched_C = 0, 0
    for i in range(len(A)):
        if A[i] == B[matched_B]:
            matched_B += 1
        else:
            matched_B = 0

        if A[i] in C:
            matched_C += 1
        else:
            matched_C = 0

        if matched_B == len(B):
            found_B = True
            matched_B = 0
        if matched_C > len(B):
            return False
    return found_B


class TestIsLongestSubarray:

    Example = namedtuple("Example", ["input", "expected"])

    examples = [
        Example(([1, 1, 5, 1, 2], [1, 2], [2, 1]), True),
        Example(([1, 2, 3], [1, 2, 3], [1, 2, 3]), True),
        Example(([0, 0, 0], [1, 2], [0, 1, 2]), False),
        Example(([1, 1, 1], [1, 1], [1]), False),
        Example(([1, 2, 3], [1], [2, 3]), False),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_is_longest_subarray(self, example):
        got = is_longest_subarray(*example.input)
        assert got == example.expected
