# LeetCode #387: First Unique Character in a String. It asks for the first non-repeating character and returns its index

input: str = "Leetcode"


class Solution:
    def firstUniqChar(self, s: str) -> int | str:
        frequency = {}

        for char in s:
            if char in frequency:
                frequency[char] += 1

            else:
                frequency[char] = 1

        for i, char in enumerate(s):
            if frequency[char] == 1:
                return i

        return -1


solution = Solution()

print(solution.firstUniqChar(input))
