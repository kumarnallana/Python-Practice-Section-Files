# data = [
#     {
#         id: 1,
#         "name": "kumar",
#         "age": 20,


#     }
# ]

# def user_login(name="User"):
#     return name


# name = input("Enter you're name??").strip()

# if (name == ""):
#     user_details = user_login()
# else:
#     user_details = user_login(name)

# print(f"Hello {user_details}")


# def collage_info(clg_name, clg_id, clg_address):
#     return clg_id, clg_name, clg_address


# clg_id, clg_name, clg_address = collage_info(
#     clg_id=2024, clg_name="kiet", clg_address="korangi, near yanam 533550")

# collage_db = f"""
# -------------------------
# Collage-Id: {clg_id},
# Collage-Name: {clg_name},
# Collage-Address: {clg_address}
# -----------------------
# """
# print(collage_db)

# def multiple_by(init_value, *numbers):
#     result = init_value

#     for num in numbers:
#         result += num
#     return result


# print(multiple_by(2, 10, 2, 1))
# print(multiple_by(2, 500))

# STR PRACTICE

# from array import array
# text = "-------@kumarNallana ---$**_ $**_ $**_ $**_ -- @@ ---------@@@"

# make_translation = str.maketrans("kumar", "Kumar", "$**_ -@")

# text_translate = text.translate(make_translation)

# print(f"Translated Text: [{text_translate}]")


# ARRAY EXAMPLE


# user_typeCode = input("Enter a TypeCode (e.g., 'i'): ")
# raw_input = input("Enter a sequence of numbers separated by spaces: ")

# numbers = [int(x) for x in raw_input.split()]

# array_data = array(user_typeCode, numbers)

# get_even_array = array(array_data.typecode, (data for data in array_data if data %
#                        2 == 0))

# get_odd_array = array(array_data.typecode, (data for data in array_data if data %
#                                             2 != 0))

# get_even_array.reverse()
# print(f"Even Array_data : {get_even_array.tolist()}")
# print(f"Odd Array_data : {get_odd_array.tolist()}")


# FACTORIAL IN PYTHON

# user_input = int(input("Enter a number to know factorial..!!"))


# def factorial(number):
#     res = 1
#     for i in range(res, number+1):
#         res *= i
#     return res


# print(f"Factorial of {user_input} is {factorial(user_input)}")


# RECURSION IN PYTHON
# import sys
# from time import sleep

# count = 1


# def sum():
#     global count
#     if count >= 10:
#         count = 10
#     count += 1
#     # sleep(0.02)
#     sum()


# print(sum())


# sys.setrecursionlimit(1000000)
# print(sys.getrecursionlimit())

# FACTORIAL USING RECURSION

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)


# result = factorial(15)

# print(result)


# HOD & LAMDA

"""Example - 1"""

# def square(num):
#     return num ** 2


# def cube(num):
#     return num ** 3


# def math_operation(num, operaion):
#     return operaion(num)


# total_result_square = math_operation(5, square)
# total_result_cube = math_operation(5, cube)

# print(total_result_square)
# print(total_result_cube)

# Py Lambda function to return even or odd based on USER INPUT

# user_input = int(input("Enter a number (eg: 0 - 99)"))
# logic = lambda n : "You Entered a Odd Number" if n % 2

# print(list(logic))


# Filter in python
# from functools import reduce

# # EXAMPLE - 1
# numbers = [10, 55, 32, 75, 90, 41, 68]
# greater_num = list(filter(lambda n: n > 50, numbers))
# double_it = list(map(lambda n: n * 2, greater_num))
# sum_of_doubles = reduce(lambda n, m: n + m, double_it)
# print(greater_num)
# print(double_it)
# print(sum_of_doubles)


# # EXAMPLE - 1
# numbers = [2, 3, 4]
# cube_of_numbers = list(map(lambda n: n ** 3, numbers))
# sum_of_cubes = reduce(lambda a, b: a + b, cube_of_numbers)


# print(cube_of_numbers)
# print(sum_of_cubes)

# Inner function

# def outer():
#     print("Outer message..!!")

#     def inner(number):
#         print("inner message..!!", number)
#     return inner


# something = outer()
# something(20)


# DECORATORS IN PYTHON

# def main_func(func):
#     def wrap(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)
#     return wrap


# def log_info(func):
#     def log_wrap(a, b):
#         print(f"Given Values: {a, b}")
#         result = func(a, b)
#         print(f"Result: {result}")
#     return log_wrap


# @main_func
# @log_info
# def substract_func(a, b):
#     return a - b


# @main_func
# @log_info
# def divide_func(a, b):
#     return a/b


# sum_total = divide_func(3, 4)
# divide_total = substract_func(3, 4)

# print(sum_total)
# print(divide_total)


# import re as regex

# email = input("Enter you're email??")
# pattern = r'^[A-Za-z0-9._-]+@[A-Za-z-0-9.]+\.[A-Za-z]{2,}$'

# if regex.fullmatch(pattern, email):
#     print("entered a valid email")
# else:
#     print("entered a invalid email")

# import pdb

# def divide(a, b):
#     pdb.set_trace()
#     return a / b

# print(divide(10, 2))

while True:
    try:
        a = int(input("Enter your first num? "))
        b = int(input("Enter your second num? "))

        result = a / b
        print(f"Result: {result}")

        break

    except ValueError:
        print("Invalid input! Please enter numbers only.", end="\n")

    except ZeroDivisionError:
        print("You cannot divide by zero! Try again.", end="\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}", end="\n")
