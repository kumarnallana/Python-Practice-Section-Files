
# Problem 1: Valid Palindrome

# Task: Given a string/array, determine if it reads the same backward as forward.

# Logic: Check if arr[left] == arr[right]. If equal, left += 1 and right -= 1. If not, return False.

# numbers: list[int] = [2, 1, 2, 3, 2, 1]
# person_name: str = "mracfeecar"


# def manual_length(arr):
#     count = 0
#     for _ in arr:
#         count += 1
#     return count


# def valid_palindrome(sequence: list[int] | str) -> bool | None:
#     n = manual_length(sequence)

#     left = 0
#     right = n - 1

#     while left < right:
#         if sequence[left] != sequence[right]:
#             return False
#         left += 1
#         right -= 1
#     return True


# result = valid_palindrome(numbers)
# result2 = valid_palindrome(person_name)

# print(result)
# print(result2)


# Problem 2: Reverse an Array in Place

# Task: Reverse a given array without creating a new list.

# Logic: Swap arr[left] with arr[right], then move pointers inward until left >= right.


emp_name = 'Nallana'


def manual_length(arr):
    count = 0
    for _ in arr:
        count += 1
    return count


def reverse_an_arr(arr: str) -> list[str]:

    chars = [char for char in arr]

    n = manual_length(chars)

    left = 0
    right = n - 1

    while left < right:
        if chars[left] != chars[right]:
            chars[right], chars[left] = chars[left], chars[right]

            left += 1
            right -= 1
    return chars


print(reverse_an_arr(emp_name))
