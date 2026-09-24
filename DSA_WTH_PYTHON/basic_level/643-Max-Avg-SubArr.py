nums: list[int] = [1, 12, -5, -6, 50, 3]
k: int = 4


class Solution:

    def manual_length(self, nums: list[int]) -> int:
        count = 0

        for _ in nums:
            count += 1

        return count

    def max_avg_arr(self, nums: list[int], K: int) -> float:
        n = self.manual_length(nums)

        left = 0
        right = 0

        current_sum = 0
        max_sum: int | None = None

        while right < n:

            current_sum += nums[right]

            if right - left + 1 == K:

                if max_sum is None or current_sum > max_sum:
                    max_sum = current_sum

                current_sum -= nums[left]
                left += 1

            right += 1

        assert max_sum is not None

        average = max_sum / K

        return average


solution = Solution()

print(solution.max_avg_arr(nums=nums, K=k))
