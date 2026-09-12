from functools import reduce

nums = [24, 33, 55, 66, 74, 5, 6, 9, 8]


filter_even = list(filter(lambda n: n % 2 == 0, nums))
print(filter_even)

double_it = list(map(lambda n: n * 2, filter_even))
print(double_it)

sum = reduce(lambda x, y: x + y, double_it)
print(sum)
