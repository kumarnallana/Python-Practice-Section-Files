# Given a string s, find the length of the longest substring without duplicate characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

class Solution:
    def manual_length(self, arr: str) -> int:
        count = 0
        for _ in arr:
            count += 1
        return count

    def getLongestSubstring(self, s: str) -> tuple[int, str]:
        n = self.manual_length(s)
        left = 0
        right = 0
        max_length = 0
        start_index = 0  # 👈 Tracks where the longest substring begins

        while right < n:
            k = left
            duplicate_position = -1

            while k < right:
                if s[k] == s[right]:
                    duplicate_position = k
                    break
                k += 1

            if duplicate_position != -1:
                left = duplicate_position + 1

            current_length = right - left + 1

            # When a new maximum is found, update max_length AND start_index
            if current_length > max_length:
                max_length = current_length
                start_index = left  # 👈 Save the start position

            right += 1

        # Extract the substring
        longest_str = s[start_index: start_index + max_length]

        return max_length, longest_str


frequent_substring = "kummars"

result = Solution()
length, substr = result.getLongestSubstring(frequent_substring)

print(f"Length of longest substring: {length}")
print(f"The longest substring is: '{substr}'")
print(f"Characters in substring: {[char for char in substr]}")
