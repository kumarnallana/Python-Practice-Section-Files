nums = [-4, -1, 0, 3, 10]


class SqaureRoot:
    def manual_length(self, arr: list[int]):
        count = 0

        for _ in arr:
            count += 1

        return count

    def multiply_arr(self, arr: list[int]):
        n = self.manual_length(arr)
        result = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:
            left_sq = arr[left] ** 2
            right_sq = arr[right] ** 2

            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1

        return result


square_root = SqaureRoot()

print(square_root.multiply_arr(nums))
