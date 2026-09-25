

nums = [1, 2, 2, 3, 3, 3]


def unique_val(nums: list[int]) -> int:

    if not nums:
        return 0

    seen = set()

    count: int = 0

    for num in nums:
        if num not in seen:
            seen.add(num)
            count += 1

    return count


print(unique_val(nums))
