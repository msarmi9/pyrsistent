def reverse_chars_in_place(chars: list[str]) -> list[int]:
    """Reverse a list of characters in-plae."""
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


def reverse_words_in_place(chars: list[str]):
    """Reverse a list of space-delineated words in-place."""
    reverse_chars_in_place(chars)
    spaces = [-1] + [ix for ix, char in enumerate(chars) if char == " "] + [len(chars)]
    for i in range(1, len(spaces)):
        left, right = spaces[i - 1] + 1, spaces[i] - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1


class TestReverseWords:
    def test_one_words(self):
        inp = list("dog")
        expected = list("dog")
        reverse_words_in_place(inp)
        assert inp == expected

    def test_two_words(self):
        inp = list("a dog")
        expected = list("dog a")
        reverse_words_in_place(inp)
        assert inp == expected
