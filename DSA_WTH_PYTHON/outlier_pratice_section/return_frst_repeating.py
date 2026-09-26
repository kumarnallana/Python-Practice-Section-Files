nums: list[int] = []


def return_repeating_num(nums: list[int]) -> int | None:

    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)

        elif num in seen:
            return num

    return None


print(return_repeating_num(nums))
