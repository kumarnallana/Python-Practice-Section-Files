nums: list[int] = [0, 0, 1, 1]


class Solution:

    def manual_length(self, nums: list[int]) -> int:
        count: int = 0
        for _ in nums:
            count += 1

        return count

    def removeDuplicates(self, nums: list[int]) -> int:
        n = self.manual_length(nums)
        slow = 0
        fast = 0
        seen = set()

        while fast < n:

            if nums[fast] not in seen:
                nums[slow] = nums[fast]
                slow += 1
                seen.add(nums[fast])

            fast += 1

        return slow


solution = Solution()

print(solution.removeDuplicates(nums))
