# LeetCode 27: Remove Element

# Pattern: Two Pointers → Same Direction → Slow/Fast Pointers → In-place Array Modification

# Problem

# Given an integer array nums and an integer val, remove every occurrence of val in-place and return the number of elements that are not equal to val.

nums = [3, 2, 2, 3, 2, 4, 5]
val = 3


class Solution:
    def manual_length(self, nums: list[int]) -> int:
        count: int = 0

        for _ in nums:
            count += 1

        return count

    def remove_element(self, nums: list[int], value: int):
        n = self.manual_length(nums)  # total length of arr[int]
        slow = 0
        fast = 0

        while fast < n:
            if nums[fast] != value:
                # storing k element into the nums[0] indexwhich is not equal to value
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow


solution = Solution()
print(solution.remove_element(nums, val))
