"""
Coffee Scheduler

Meet Lara & Lars, two good friends and two very busy engineers. Lara & Lars like to grab coffee
once a week to catch up, but it's a total headache to find a time during which they're both
free, so they decide to automate the pain away.

Their daily free time can be represented as a sorted array of disjoint time intervals, with
each interval indicating a free block's start and end time. For example, Monday's free blocks
look like:

Lara: [(8, 9), (12, 13), (15, 17), (18, 20)]
Lars: [(7, 8), (10, 13), (14, 16), (17, 18), (19, 22)]

The times where they're both free to grab a coffee look like:

Coffee: [(12, 13), (15, 16), (19, 20)]

Write a function that takes their scheduled free time as input and returns a single array
containing all blocks during which they're both free.
"""

from collections import namedtuple

Block = namedtuple("Block", ["start", "end"])


def intersect(A: list[Block], B: list[Block]) -> list[Block]:
    """Return the intersection of two lists of sorted disjoint time blocks."""
    intersection = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        a, b = A[i], B[j]
        if a.end < b.end:
            if a.end > b.start:
                start = max(a.start, b.start)
                intersection.append(Block(start, a.end))
            i += 1
        else:
            if a.start < b.end:
                start = max(a.start, b.start)
                intersection.append(Block(start, b.end))
            j += 1
    return intersection


class TestIntersect:
    """Tests `intersect` on the four possible block scenarios."""

    def test_case_where_blocks_intersect_at_most_one_block(self):
        lara = [Block(8, 9), Block(12, 13), Block(15, 17), Block(18, 20)]
        lars = [Block(7, 8), Block(10, 13), Block(14, 16), Block(17, 18), Block(19, 22)]
        expected = [Block(12, 13), Block(15, 16), Block(19, 20)]
        got = intersect(lara, lars)
        assert got == expected

    def test_case_where_blocks_intersect_multiple_blocks(self):
        lara = [Block(8, 11), Block(12, 16), Block(17, 19)]
        lars = [Block(10, 14), Block(15, 18)]
        expected = [Block(10, 11), Block(12, 14), Block(15, 16), Block(17, 18)]
        got = intersect(lara, lars)
        assert got == expected

    def test_case_where_no_block_intersects_another_block(self):
        lara = [Block(5, 8), Block(12, 14), Block(16, 20)]
        lars = [Block(8, 10), Block(14, 16)]
        expected = []
        got = intersect(lara, lars)
        assert got == expected

    def test_case_where_one_block_intersects_all_other_blocks(self):
        lara = [Block(5, 8), Block(12, 14), Block(16, 20)]
        lars = [Block(0, 24)]
        expected = lara
        got = intersect(lara, lars)
        assert got == expected
