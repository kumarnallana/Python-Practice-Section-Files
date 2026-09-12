# WHILE LOOP
# user_input = input("Enter your Name we will print multiple times 🌚").strip()

# count = 0
# while (count < 5):
#     print(user_input)
#     count += 1

# RANGE IN PYTHON

# METHOD - 1 WTH ONE PARAMETER

# user_input = int(input("Enter a Range of number?").strip())

# range_of_data = range(user_input)
# print(range_of_data)

# list_range = list(range_of_data)
# print(list_range)

# METHOD - 2 WTH TWO PARAMETER  IN RANGE
# user_name = input("Enter your name?")
# user_frst_para = int(input("Enter your frst range(Eg: 0 - 99)").strip())
# user_frst_para2 = int(input("Enter your Second range(Eg: 0 - 99)").strip())

# choosen_ranges = range(user_frst_para, user_frst_para2)

# print(choosen_ranges)

# if (user_frst_para <= 99 and user_frst_para2 <= 99):
#     list_of_ranges = list(choosen_ranges)
#     print(list_of_ranges)
# else:
#     print(f"{user_name},You need to Choose a valid Range from 0 to 99 ⚠️ ")

# METHOD - 3 WTH THREE PARAMETERS IN RANGE
# user_name = input("Enter your name?")
# user_frst_para = int(input("Enter your frst range(Eg: 0 - 99)").strip())
# user_frst_para2 = int(input("Enter your Second range(Eg: 0 - 99)").strip())
# user_condition_para = int(input(
#     "Enter the times you wanted to repeat the range(Eg:2 tym's or 3 tyme's...n tyme's)").strip())

# choosen_ranges = range(user_frst_para, user_frst_para2, user_condition_para)

# print(choosen_ranges)

# if (user_frst_para <= 99 and user_frst_para2 <= 99 and 0 <= user_condition_para <= 20):
#     list_of_ranges = list(choosen_ranges)
#     print(list_of_ranges)
# else:
#     print(f"{user_name},You need to Choose a valid Range from 0 to 99 ⚠️")
#     print("And you need to mention beyond 20 tym's(eg: 1 - 19) ⚠️")


# METHOD - 4 WTH THREE PARAMETERS IN RANGE USING TUPLES
# user_name = input("Enter your name?")
# user_frst_para = int(input("Enter your frst range(Eg: 0 - 99)").strip())
# user_frst_para2 = int(input("Enter your Second range(Eg: 0 - 99)").strip())
# user_condition_para = int(input(
#     "Enter the times you wanted to repeat the range(Eg:2 tym's or 3 tyme's...n tyme's)").strip())

# choosen_ranges = range(user_frst_para, user_frst_para2, user_condition_para)

# print(choosen_ranges)

# if (user_frst_para <= 99 and user_frst_para2 <= 99 and 0 <= user_condition_para <= 20):
#     tuples_of_ranges = tuple(choosen_ranges)
#     print(tuples_of_ranges)
# else:
#     print(f"{user_name},You need to Choose a valid Range from 0 to 99 ⚠️")
#     print("And you need to mention beyond 20 tym's(eg: 1 - 19) ⚠️")

# FOR LOOP IN PYTHON
# list_of_data = ["banana", "mango", "pineapple", "apple", "lemon"]

# for fruit in list_of_data:
#     print(fruit)

# RANGE IN FOR LOOP
# for range_seq in range(0, 10):
#     print(range_seq * 2)

# for range_seq in range(50):
#     if (range_seq % 5 == 0):
#         print(range_seq)

# list_of_data = [2, 4, 6, 55, 77, 8, 23, 45]

# for data in range(len(list_of_data)):
#     print(f"{data} At {list_of_data[data]}")

# emp_data = {"emp_id": [101, 203, 405, 504], "emp_name": [
#     "kumarNallana", "prudhvi", "rajesh", "Bhavya"],
#     "emp_role": ["Dev", "Cloud", "Devops", "ml"]
# }

# for emp_id, emp_name, role in zip(*emp_data.values()):
#     print(f"e-id: {emp_id} || e-name: {emp_name} || e-role: {role}")

# std_scores = [[25, 45, 66, 87, 90], [34, 22, 1, 45, 78], [45, 89, 100, 28]]

# for std_list in std_scores:
#     # print(std_list, end=" ")
#     for std_score in std_list:
#         print(std_score, end=" ")

# MULTIPLICATON USING FOR LOOOP

# user_frst_para = int(input("Enter your frst range(Eg: 0 - 99)").strip())
# user_frst_para2 = int(input("Enter your Second range(Eg: 0 - 99)").strip())
# user_condition_para = int(input(
#     "Enter the times you wanted to repeat the range(Eg:2 tym's or 3 tyme's...n tyme's)").strip())

# for user_input in range(user_frst_para, user_frst_para2, user_condition_para):
#     print(f"{user_frst_para} x {user_input} = {user_frst_para * user_input}")

# TABLE MULTIPLICATION BY USING USER INPUT

# user_frst_para = int(input("Enter your frst range(Eg: 0 - 10)").strip())
# user_frst_para2 = int(input("Enter your Second range(Eg: 0 - 10)").strip())

# for user_input in range(user_frst_para, user_frst_para2):
#     if user_input == 0:
#         continue
#     for table in range(1, 11):
#         print(f"{user_input} x {table} = {user_input*table}")
#     print()

# start = int(input("Enter your frst range(Eg: 0 - 10)").strip())
# stop = int(input("Enter your Second range(Eg: 0 - 10)").strip())

# start = 4
# stop = 10
# for m in range(1, stop+1):
#     print(f"{start} x {m} = {start*m}")
# print()

# Enumerate in loops

# languages = ["english", "Tamil", "Hindi", "Kannada", "Telugu"]

# enumerated_list = list(enumerate(languages))
# print(enumerated_list)

# languages = ['Spanish', 'English', 'Russian', 'Chinese']

# for index, language in enumerate(languages):
#     print(f'Index {index} and language {language}')

# languages = ['Spanish', 'English', 'Russian', 'Chinese']

# for index, language in enumerate(languages, 1):
#     print(f'Index {index} and language {language}')

# emp_names = {"Name": ["kumarNallana", "prudhvi", "Rajesh", "Raja", "Bhavya"]}
# emp_ids = {name: i for i, name in enumerate(emp_names["Name"], start=404)}

# print(emp_ids)

# ZIP FUNCTION  IN LOOPS
emp_names = {"kumarNallana", "prudhvi", "Rajesh", "Raja", "Bhavya"}
ids = [404, 405, 406, 407, 408]

emp_data = dict(zip(emp_names, ids))
for name, ids in emp_data.items():
    print(f"Emp_name: {name} || Emp_id: {ids}")
