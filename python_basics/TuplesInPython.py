# TUPLES IN PYTHON
# Tuple is immutable (elements cannot be changed after creation) and it is declared using parentheses (); it is used when data should remain constant.


"""
tuple_type = (10, 20, "KUmar")

print(tuple_type)

print(type(tuple_type))

tuple2 = (10)
print(tuple2)
# IT RETURNS A INT WHICH IS STARANGE BCZ WE DIDN'T MENTIONED THE SECOND TYPE OR OTHER DATA AFTER 10 OR ","
print(type(tuple2))

tuple3 = (10,)
# NOW IT WILL BE TUPLE BCZ WE MENTIONED THE "," SO EMPTY TUPLE TYPE CONSIDERED AS THE INT TYPE
print(type(tuple3))

# Most used Python tuple methods / operations (developer usage):
# count(), index(), len(), max(), min(), sum(), sorted()

tupleLength = ("kumar", 25, True, 200371)
t = (1, 2, 3, 2, 105, 9, 99, 5)
t2 = (22, 3, 7, 7, 7, 34, 5, 6, 7, 8, 24)
print(len(tupleLength))
print("-------")

# INDEXING
print(tupleLength[0])
print(tupleLength[1: 3])#SLICING
print(tupleLength[-1])
print(tupleLength.index(True))
print(t.count(2))
print(t2.count(7))

print("-------")

# MATHS OPERATIONS
print(max(t))
print(min(t))
print(sum(t))
print(t2 >= t)
print(t2 >= t)
print(sorted(t2))
print(sorted(t))
print(t in t2)
print(t not in t2)
print("-------")"""

# DESTRUCTURING IN TUPLES
# METHOD-1
user = ("kumar", 21, "Frontend Dev", 20371, ("viravada", "Ap", 533450))
name, age, role, emp_id, *user_address = user
print(name)
print(age)
print(role)
print(emp_id)
print(user_address)

# METHOD-2
name2, age2, role2, emp_id2, _ = user
print(age2)
print(_)

# METHOD-3
single_item = (10,)
value, *nothing_left = single_item

print(value)        # 10
print(nothing_left)  # []  <-- Empty list!

# METHOD-4 NESTED UNPACKING
name, *_, (city, state, pincode) = user
print(city)
print(_)
