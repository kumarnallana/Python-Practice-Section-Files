nums: list[int] = [0, 0, 1, 1]


class Solution:

    def manual_length(self, nums: list[int]) -> int:
        count: int = 0
        for _ in nums:
            count += 1

        return count

    def removeDuplicates(self, nums: list[int]) -> int:
        n = self.manual_length(nums)
        slow = 1
        fast = 1

        while fast < n:

            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow


solution = Solution()

print(solution.removeDuplicates(nums))
