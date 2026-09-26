def char_count(words: list[str]) -> int:
    count: int = 0
    letter: str = "a"

    for word in words:
        if not word:
            continue

        if word[0].lower() == letter:
            count += 1

    return count


words = ["Apple", "", "banana", "ant", "Air", "cat"]

print(char_count(words))
