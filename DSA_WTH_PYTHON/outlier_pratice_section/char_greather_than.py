words = ["cat", "apple", "dog", "tree", "banana"]


def greater_than(words: list[str]) -> int:
    count: int = 0

    for word in words:
        if not word:
            continue

        if len(word) > 3:
            count += 1

    return count


print(greater_than(words))
