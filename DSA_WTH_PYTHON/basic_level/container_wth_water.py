
class Solution:
    def manual_length(self, height: list[int]) -> int:
        count = 0
        for _ in height:
            count += 1
        return count

    def maxArea(self, height: list[int]) -> int:
        n = self.manual_length(height)
        left = 0
        right = n - 1
        max_water = 0

        while left < right:
            width = right - left

            if height[left] < height[right]:
                h = height[left]
                area = width * h
                left += 1

            else:
                h = height[right]
                area = width * h
                right -= 1
            if area > max_water:
                max_water = area
        return max_water
