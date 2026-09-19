person_name: str = "ku_mar-"


class Solution:

    def manual_length(self, s: str) -> int:
        count: int = 0

        for _ in s:
            count += 1

        return count

    def reverseOnlyLetters(self, s: str) -> str:
        n = self.manual_length(s)

        characters: list[str] = list(s)

        left = 0
        right = n - 1

        while left < right:

            is_left_letter = (
                'a' <= characters[left] <= 'z'
                or
                'A' <= characters[left] <= 'Z'
            )

            is_right_letter = (
                'a' <= characters[right] <= 'z'
                or
                'A' <= characters[right] <= 'Z'
            )

            if not is_left_letter:
                left += 1

            elif not is_right_letter:
                right -= 1

            else:
                characters[left], characters[right] = (
                    characters[right],
                    characters[left]
                )

                left += 1
                right -= 1

        return "".join(characters)


solution = Solution()

print(solution.reverseOnlyLetters(person_name))
