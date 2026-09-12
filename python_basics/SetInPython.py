"""
    Set is mutable, unordered, and stores only unique elements (duplicates are not allowed). Sets are declared using curly braces {} or the set() function.

Most used Python set methods / operations (developer usage):
add(), update(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference(), len(), max(), min(), Membership (in / not in).
    """
"""
set_fun = {1, 5, 6, 8, 68, 4, 3, 7, 98, 90}
print(set_fun)

# UPDATING & MODIFICATION OPERATIONS
set_fun.add(909)
print(set_fun)
# set2 = set
set2 = set()
set2.update([708, 203, 305, 101])
print(set_fun)
print("Updated Set2 =", set2)
set2.remove(708)
print("REmoved Set2", set2)
"""

"""The .discard() method is the "safe" way to remove an element from a set. Unlike .remove(), which throws a KeyError if the element isn't found, .discard() simply does nothing if the value is missing. It’s like saying, "If it's there, get rid of it; if not, don't worry about it."
    """
# set2.discard(0)
# print("Discarded Set", set2)

# my_set = {101, 203, 305, 708}

# Pop an item and store it in 'item'

# print("Actual item:", my_set)

# item = my_set.pop()
# print(f"Removed item: {item}")
# print(f"Remaining set: {my_set}")

# my_set.clear()
# print(my_set)  # Output: set()
# The set is still there, it's just empty!


fruits_list1 = {"Pineapple", "Honeydew",
                "Starfruit", "Watermelon", "Blueberry", 55, 22, 1}

fruits_list2 = {"Strawberry", "Raspberry",
                "Blueberry", "Blackberry", "Watermelon", 55, 1}

# set_union = fruits_list1 | fruits_list2
# set_union2 = fruits_list1.union(fruits_list2)
# print(set_union)
# print(set_union2)

# set_diff = fruits_list2 - fruits_list1
# set_diff2 = fruits_list1.difference(fruits_list2)
# print(set_diff)
# print(set_diff2)

# set_intersecton = fruits_list1 & fruits_list2
# set_intersecton2 = fruits_list1.intersection(fruits_list2)
# print(set_intersecton)
# print(set_intersecton2)

# set_symmetricdiff = fruits_list1.symmetric_difference(fruits_list2)
# set_symmetricdiff2 = fruits_list1 ^ fruits_list2
# print(set_symmetricdiff)
# print(set_symmetricdiff2)

# isdisjoint() returns True if two sets have no common elements; otherwise it returns False.
# set_disjoint = fruits_list1.isdisjoint(fruits_list2)
# print(set_disjoint)

set_num = {1, 2, 3, 4, 5, 6}
set_num2 = {1, 2, 3, 4, 5, 6, 7, 8, 11}

# set_is_subset = set_num.issubset(set_num2)
# print(set_is_subset)

# set_is_superset = set_num.issuperset(set_num2)
# set_is_superset2 = set_num2.issuperset(set_num)
# print(set_is_superset)
# print(set_is_superset2)

# print(max(set_num2))
# print(min(set_num2))
# print(len(set_num2))

# Membership (in / not in).
print("banana" in fruits_list2)
print(2 in set_num)
print("kumar" not in fruits_list2)
