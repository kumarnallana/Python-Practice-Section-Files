def second_largest(nums):
    largest = None
    second = None

    for num in nums:
        if largest is None or num > largest:
            if num != largest:
                second = largest
                largest = num

        elif num != largest and (second is None or num > second):
            second = num

    return second


print(second_largest([5, 4, 3]))
# 4

print(second_largest([1, 2, 2]))
# 1

print(second_largest([-5, -2, -8]))
# -5

print(second_largest([5, 5, 5]))
# None
