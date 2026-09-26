nums: list[int] = [4, 5, 6, 5, 7]


def frst_non_repeating_num(nums: list[int]) -> int | None:

    frequency: dict = {}

    for num in nums:
        if num in frequency:
            frequency[num] += 1

        else:
            frequency[num] = 1

    for num in nums:
        if frequency[num] == 1:
            return num

    return None


print(frst_non_repeating_num(nums))
