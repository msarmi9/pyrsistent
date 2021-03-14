"""
Climbing the Leaderboard

The leaderboard of an arcade game is represented as a descending array of ints and ech
player's game scores are represented by an ascending array of ints. For example,

Leaderboard: [100, 90, 90, 80]
Player: [70, 80, 105]

Our task is to write a function that takes the above two arrays as input and returns an
array listing the rank of each of the player's scores.

For example, the above leaderboard has rankings [1, 2, 2, 3] and the player's rankings after each
game are [4, 3, 1].
"""

from collections import namedtuple
from typing import Any

import pytest


def get_rankings(leaderboard: list[int], scores: list[int]) -> list[int]:
    """Compute the rank of each player score relative to a fixed leaderboard."""
    leaderboard = unique(leaderboard)
    idx = len(leaderboard) - 1
    ranks = []

    for score in scores:
        found = False
        while not found:
            if score > leaderboard[0]:
                ranks.append(1)
                found = True
            elif score == leaderboard[idx]:
                ranks.append(idx + 1)
                found = True
            elif score < leaderboard[idx]:
                ranks.append(idx + 2)
                found = True
            else:
                idx -= 1
    return ranks


def unique(lst: list[Any]) -> list[Any]:
    """Construct a new list without duplicates."""
    seen, res = set(), []
    for el in lst:
        if el not in seen:
            res.append(el)
            seen.add(el)
    return res


class TestRankings:
    """Tests `get_rankings` on various scoring scenarios."""

    Example = namedtuple("Example", ["leaderboard", "scores", "expected"])

    examples = [
        Example([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120], [6, 4, 2, 1]),
        Example([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102], [6, 5, 4, 2, 1]),
        Example([100, 90, 90, 80], [70, 80, 105], [4, 3, 1]),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_mixed_leaderboard_and_scores(self, example):
        got = get_rankings(example.leaderboard, example.scores)
        assert got == example.expected
