"""
Max Subarray

Given an integer array, find the largest sum of any contiguous subarray. Then find the subarrays
with this sum.
"""

from collections import namedtuple

import pytest


# Moral: sum the next elem if the resulting sum is bigger than it, else reset sum as next elem
def max_subarray_sum(A: list[int]) -> int:
    """Return the largest sum of a contiguous subarray."""
    current, largest = 0, -1e30
    for a in A:
        current = max(a, current + a)
        largest = max(current, largest)
    return largest


def find_max_subarray(A: list[int]) -> list[int]:
    """Return a contiguous subarray with the largest sum."""
    current, largest = 0, -1e30
    c_start = l_start = l_end = 0
    for c_end, a in enumerate(A):
        if current + a >= a:
            current = current + a
        else:
            current = a
            c_start = c_end
        if current >= largest:
            largest = current
            l_start = c_start
            l_end = c_end
    return A[l_start: l_end + 1]


def find_max_subarrays(A: list[int]) -> list[list[int]]:
    """Return all contiguous subarrays with the largest sum."""
    largests = []
    current, largest = 0, 1e-30
    c_start = l_start = l_end = 0
    for c_end, a in enumerate(A):
        if current + a >= a:
            current = current + a
        else:
            current = a
            c_start = c_end
        if current >= largest:
            if current > largest:
                largests = []
            largest = current
            l_start = c_start
            l_end = c_end
            largests.append(A[l_start: l_end + 1])
    return largests


class TestMaxSubarray:

    Example = namedtuple("Example", ("input", "expected_sum", "expected_subarray"))

    examples = [
        Example([-1, -2, 7], 7, [7]),
        Example([-1, -2, -3], -1, [-1]),
        Example([1, 2, 3, 4], 10, [1, 2, 3, 4]),
        Example([-1, 3, 0, -2, 5], 6, [3, 0, -2, 5]),
        Example([4, -2, 3, -1, 7], 11, [4, -2, 3, -1, 7]),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_max_subarray_sum(self, example):
        got = max_subarray_sum(example.input)
        assert got == example.expected_sum

    @pytest.mark.parametrize("example", examples)
    def test_find_max_subarray(self, example):
        got = find_max_subarray(example.input)
        assert got == example.expected_subarray

    def test_find_max_subarrays(self):
        inp = [1, 0, 0]
        expected = [[1], [1, 0], [1, 0, 0]]
        got = find_max_subarrays(inp)
        assert got == expected
