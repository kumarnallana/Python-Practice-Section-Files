
words: list[str] = ["apple", "Arora" "banana", "ant", "cat", "air"]


def char_count(words: list[str]) -> int | str:
    count = 0
    letter: str = "a"

    for word in words:
        try:
            if not word:
                raise KeyError("Words list should not be empty")
            if word[0].lower() == letter.lower():
                count += 1
        except Exception as e:
            return f"Error: {e}"

    return count


print(char_count(words))
