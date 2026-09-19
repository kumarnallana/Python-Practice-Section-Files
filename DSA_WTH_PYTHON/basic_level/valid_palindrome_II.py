class Solution:
    def manual_length(self, s: str) -> int:
        count = 0

        for _ in s:
            count += 1

        return count

    def check_palindrome(self, s: str, left: int, right: int) -> bool:

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def validPalindrome(self, s: str) -> bool:

        n = self.manual_length(s)

        left = 0
        right = n - 1

        while left < right:

            if s[left] != s[right]:

                skip_left = self.check_palindrome(
                    s,
                    left + 1,
                    right
                )

                skip_right = self.check_palindrome(
                    s,
                    left,
                    right - 1
                )

                return skip_left or skip_right

            left += 1
            right -= 1

        return True


input = "abca"

solution = Solution()

print(solution.validPalindrome(input))
