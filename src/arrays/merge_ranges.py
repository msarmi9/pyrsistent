Range = tuple[int, int]


# O(nlogn)
def merge_ranges(ranges: list[Range]) -> list[Range]:
    """Merge overlapping and adjacent ranges given a list of unordered ranges."""
    ranges = sorted(ranges)
    cur_start, cur_end = ranges[0]
    merged = []
    for start, end in ranges[1:]:
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))
    return merged


class TestMergeRanges:
    def test_merge_ranges_on_unordered_input(self):
        ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        expected = [(0, 1), (3, 8), (9, 12)]
        got = merge_ranges(ranges)
        assert got == expected

    def test_merge_ranges_on_disjoint_input(self):
        ranges = [(1, 3), (6, 8), (11, 14)]
        expected = ranges
        got = merge_ranges(ranges)
        assert got == expected

    def test_merge_ranges_on_adjacent_input(self):
        ranges = [(2, 5), (5, 7), (7, 9)]
        expected = [(2, 9)]
        got = merge_ranges(ranges)
        assert got == expected

    def test_merge_ranges_on_nested_input(self):
        ranges = [(1, 5), (1, 3), (2, 4)]
        expected = [(1, 5)]
        got = merge_ranges(ranges)
        assert got == expected
