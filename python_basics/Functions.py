# FUNCTIONS IN PYHTON

# user_name = input("enter your name?").strip()

# print(user_name, "when did the last time india won odi world cup?")

# user_day = input("Enter day?").strip()
# user_month = input("Enter month?").strip()
# user_year = input("Enter year?").strip()


# def quiz(day, month, year):
#     return f"{day}/{month}/{year}"


# ans = "24/12/2011"
# user_input = quiz(user_day, user_month, user_year)

# if (user_input == ans):
#     print(f"{user_name} you're correct 🍾🍾 india won odi world cup {user_input}")
# else:
#     print(f"Wrong answer bro❌ Right answer is {ans}")


# DEFAULT PARAMETERS IN FUNCTIONS

# def user_login(name="User"):
#     return name


# name = input("Enter your name?").strip()

# if (name == ""):
#     user_detail = user_login()
# else:
#     user_detail = user_login(name)

# print(f"Hello {user_detail}")


# NAMED PARAMETER IN FUNCTION
# def emp_data(name, id, role):
#     return name, id, role


# print(emp_data(name="kumarNallana", id=202, role="SDE"))


# VARIABLE LENGTHS ARGUMENTS IN FUNCTIONS

# # MEHTOD - 1
# def multiple_by(init_value, *numbers):
#     result = init_value

#     for num in numbers:
#         result *= num
#     return result


# print(multiple_by(2, 10, 1, 1))
# print(multiple_by(2, 500))

# MEHTOD - 2
# emp_data = {"emp_id": [101, 203, 405, 504], "emp_name": [
#     "kumarNallana", "prudhvi", "rajesh", "Bhavya"],
#     "emp_role": ["Dev", "Cloud", "Devops", "ml"]
# }


# def emps_db(data):
#     for id, name, role in zip(*data):
#         print(f"Emp_id: {id} , Emp_name: {name} , Emp_role: {role}")


# emps_db(emp_data.values())

# METHOD -3
def comp_db(**database):
    for key, value in database.items():
        print(f"Emp_{key}: {value}")


comp_db(name="kumarnallana", id="202")

# FUNCTION MODIFICATION IN PYTHON
# def fun():
#     global l
#     l = [1, 2, 3, 4]
#     # return l


# l = [10, 30, 40]
# fun()
# # print(fun(l))
# print(l)  # 1234

# def modification():
#     x = 20
#     globals()["x"] = 400
#     print(x)  # 20


# x = [2]
# modification()
# print(x)  # 400


# # RETURNING MULTIPLE VALUES IN PYTHON
# def both_operaions(x, y):
#     sum = x + y
#     multiply = x * y
#     division = x // y
#     modulus = x % y
#     exponention = x ** y
#     return [sum, multiply, division, modulus, exponention]


# print(both_operaions(2, 10))
