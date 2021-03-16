"""
Climbing the Leaderboard

The leaderboard of an arcade game is represented as an array of ints, sorted in descending order,
as are a player's scores. For example,

Leaderboard: [100, 90, 90, 80]
Player: [105, 80, 70]

Write a function that takes the above two arrays as input and returns an array listing the ranks of
each of the player's scores.

Repeated entries on the leaderboard are given equal rank, so in our above example we have

Leaderboard ranks: [1, 2, 2, 3]
Player ranks: [1, 3, 4]
"""

from collections import namedtuple

import pytest


def get_rankings(leaderboard: list[int], scores: list[int]) -> list[int]:
    """Compute the rank of each score (desc) relative to a fixed leaderboard (desc)."""
    idx, skipped = 0, 0
    ranks = []
    for score in scores:
        while idx < len(leaderboard) and score < leaderboard[idx]:
            if idx > 0 and leaderboard[idx] == leaderboard[idx - 1]:
                skipped += 1
            idx += 1
        ranks.append(idx - skipped + 1)
    return ranks


class TestRankings:
    """Tests `get_rankings` on various scoring scenarios."""

    Example = namedtuple("Example", ["leaderboard", "scores", "expected"])

    examples = [
        Example([100, 100, 50, 40, 40, 20, 10], [120, 50, 25, 5], [1, 2, 4, 6]),
        Example([100, 90, 90, 80, 75, 60], [102, 90, 77, 65, 50], [1, 2, 4, 5, 6]),
        Example([100, 90, 90, 80], [105, 80, 70], [1, 3, 4]),
    ]

    @pytest.mark.parametrize("example", examples)
    def test_mixed_leaderboard_and_scores(self, example):
        got = get_rankings(example.leaderboard, example.scores)
        assert got == example.expected
