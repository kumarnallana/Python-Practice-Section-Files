def first_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num

        seen.add(num)

    return None


print(first_duplicate([4, 7, 2, 4, 7, 4]))
