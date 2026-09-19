nums = [-4, -1, 0, 3, 10]


class Solution:

    def manual_length(self, arr: list[int]) -> int:
        count: int = 0

        for _ in arr:
            count += 1

        return count

    def sqaure_root(self, arr: list[int]) -> list[int]:
        n = self.manual_length(arr)
        result = [0] * n
        left = 0
        right = n - 1
        position = n - 1

        while left <= right:
            left_sqr = arr[left] ** 2
            right_sqr = arr[right] ** 2

            if left_sqr > right_sqr:
                result[position] = left_sqr
                left += 1

            else:
                result[position] = right_sqr
                right -= 1
            position -= 1

        return result


solution = Solution()

print(solution.sqaure_root(nums))
