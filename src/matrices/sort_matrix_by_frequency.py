"""
Sort Matrix By Frequency

Given an integer square matrix, sort its elements by ascending frequency, then ascending value.
Place the sorted elements along the anti-diagonals starting in the bottom right-hand corner.

For example, given the matrix

[[1, 4, -2],
 [-2, 3, 4],
 [3, 1, 3]]

its sorted elements are [-2, -2, 1, 1, 4, 4, 3, 3, 3] and the sorted matrix is

[[3, 3, 4],
 [3, 4, 1],
 [1, -2, -2]]
"""

from collections import Counter
from collections import namedtuple

import pytest


Matrix = list[list[int]]


def sort_by_frequency(M: Matrix) -> Matrix:
    """Sort a square matrix by asc (frequency, value), with elements placed on anti-diagonals."""
    n = len(M)
    els = sort_elements(M)
    out = [[0] * n for _ in range(n)]
    for k, (i, j) in enumerate(antidiagonal_ixs(n, reverse=True)):
        out[i][j] = els[k]
    return out


def antidiagonal_ixs(n: int, reverse=False):
    """Generate the coordinates (i, j) of the anti-diagonals of an n x n matrix from L to R."""
    n_diags = 2*n - 1
    diags = range(n_diags - 1, -1, -1) if reverse else range(n_diags)
    for d in diags:
        for k in range(d + 1):
            l = d - k
            if k < n and l < n:
                yield (l, k) if reverse else (k, l)


def sort_elements(M: Matrix, reverse=False) -> list[int]:
    """Return the elements of a matrix sorted by frequency, then value."""
    els = [el for row in M for el in row]
    counts = Counter(els)
    return sorted(els, key=lambda el: (counts[el], el), reverse=reverse)


class TestSortByFrequency:

    Example = namedtuple("Example", ("input", "expected"))

    examples = [
        Example([[1, 4, -2],
                 [-2, 3, 4],
                 [3, 1, 3]],

                [[3, 3, 4],
                 [3, 4, 1],
                 [1, -2, -2]]),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_sort_by_frequency(self, example):
        got = sort_by_frequency(example.input)
        assert got == example.expected
