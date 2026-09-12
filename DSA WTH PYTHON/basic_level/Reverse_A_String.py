class Solution:
    def manual_length(self, arr: list[str]) -> int:
        count = 0
        for _ in arr:
            count += 1
        return count

    def reverseString(self, s: list[str]) -> str:
        n = self.manual_length(s)
        left = 0
        right = n - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            return s


reverse_string = Solution()

person_data = ["k", "u", "m", "a", "r"]

result = reverse_string.reverseString(person_data)

print(result)
