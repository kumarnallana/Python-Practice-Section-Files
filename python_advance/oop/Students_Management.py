small_list: list[int] = [40, 20, 30, 40, 50, 10, 11, 12, 14, 15, 16, 17]


def linear_search(arr: list[int], target: int) -> tuple[bool, int]:
    steps = 0
    found = False

    for item in arr:
        steps += 1
        if item == target:
            found = True
            break
    return found, steps


print(linear_search(small_list, 1000))
