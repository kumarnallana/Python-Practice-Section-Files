coding_platform: str = "leetcode"


class Solution:

    def manual_length(self, words: list[str]) -> int:

        count = 0

        for _ in words:
            count += 1

        return count

    def reverse_vowel(self, words):
        n = self.manual_length(words)
        left = 0
        right = n - 1
        vowels = "aeiou"

        list_of_words: list[str] = list(words)

        while left < right:

            if list_of_words[left].lower() not in vowels.lower():
                left += 1

            elif list_of_words[right].lower() not in vowels.lower():
                right -= 1

            else:
                list_of_words[left], list_of_words[right] = list_of_words[right], list_of_words[left]
                left += 1
                right -= 1

        return "".join(list_of_words)


solution = Solution()

print(solution.reverse_vowel(coding_platform))
