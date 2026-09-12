
numbers: list[int] = [2, 4, 5, 6, 8, 11, 15]


def manual_length(arr: list[int]) -> int:
    count = 0
    for _ in arr:
        count += 1
    return count


def two_pointer_sum(arr: list[int], target: int):
    n = manual_length(arr)

    left = 0
    right = n - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


target = 22

result = two_pointer_sum(numbers, target)

if result:
    num1, num2 = result
    print(f'The Combination is {num1} + {num2} = {target}')
else:
    print("NO Combination Found!")
