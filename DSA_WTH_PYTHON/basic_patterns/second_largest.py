# nums = [10, 5, 20, 15]


# def second_largest(nums):
#     largest = nums[0]
#     second = nums[0]

#     for num in nums:
#         if num > largest:
#             second = largest
#             largest = num

#         elif num > second and num < largest:
#             second = num

#     return second


# print(second_largest(nums))


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
