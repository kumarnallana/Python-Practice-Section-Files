class BinarySearch:

    def manual_length(self, number: list) -> int:

        count = 0
        for _ in number:
            count += 1
        return count

    def search(self, number: list, target: int):
        n = self.manual_length(number)

        low = 0
        high = n - 1
        step = 0

        while low <= high:
            mid = (low + high) // 2
            step += 1

            if number[mid] == target:
                return f"Given {target} : We got middle value {number[mid]} at {step}"

            elif number[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1


data = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]

binary_search = BinarySearch()

print(binary_search.search(data, 23))
