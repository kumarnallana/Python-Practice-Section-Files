# Find the maximum sum of any 3 consecutive numbers.

nums = [2, 1, 5, 1, 3, 2]
k = 3


class Solution:

    def manual_length(self, nums: list[int]) -> int:
        count = 0
        for _ in nums:
            count += 1

        return count

    def max_sum_arr(self, nums: list[int], k) -> int:
        n = self.manual_length(nums)
        right = 0
        left = 0

        current_sum = 0
        max_sum = 0

        while right < n:

            current_sum += nums[right]

            if right - left + 1 == k:

                if current_sum > max_sum:
                    max_sum = current_sum

                current_sum -= nums[left]
                left += 1

            right += 1

        return max_sum


solution = Solution()

print(solution.max_sum_arr(nums, k))
