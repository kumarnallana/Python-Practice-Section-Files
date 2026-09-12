# LIST COMPREHENSIONS & ALSO TERNARY OPERATOR IN PYTHON
# calc_num = [(data, "Even") if data % 2 == 0 else (data, "Odd")
#             for data in range(1, 21, 1)]

# print(calc_num)

# REAL WORLD EXAMPLE WITH LIST COMPREHENSION AND TERNARY OPERATOR

# METHOD - 1
# import random  # FOR UNIQUES ID GENERATION
# emp_names = ["kumarNallana", "prudhvi", "Rajesh", "Raja", "Bhavya"]
# emp_ids = {random.randint(100, 999): name for name in emp_names}
# emp_types = ["Long" if len(emp_names) >
#              6 else "Short" for emp_name in emp_names]
# emps_data = zip(emp_ids, emp_names, emp_types)
# for ids, name, type in emps_data:
#     print(f"id: {ids} EmpName : {name} Has a {type}")

# METHOD - 2 IN A MORE READABLE WAY ✅✅

# import random  # FOR UNIQUES ID GENERATION
# emp_names = ["kumarNallana", "prudhvi", "Rajesh", "Raja", "Bhavya"]
# emp_data = [{
#     "emp_id": random.randint(100, 999),
#     "emp_Name": emp_name,
#     "Type": "Long" if len(emp_name) > 6 else "Short"
# }
#     for emp_name in emp_names
# ]


# for emp in emp_data:
#     print(
#         f"id: {emp["emp_id"]} || EmpName: {emp["emp_Name"]} || Has a {emp["Type"]} Name")

# METHOD - 3
import random
from types import SimpleNamespace

emp_names = ["kumarNallana", "prudhvi", "Rajesh", "Raja", "Bhavya"]

# Wrap the dictionary in SimpleNamespace()
emp_data = [
    SimpleNamespace(
        emp_id=random.randint(100, 999),
        emp_Name=name,
        Type="Long" if len(name) > 6 else "Short"
    )
    for name in emp_names
]

for emp in emp_data:
    # Now you CAN use dot notation!
    print(f"id: {emp.emp_id} || EmpName: {emp.emp_Name} || Has a {emp.Type} Name")

# OPTIONAL CONTENT ABOUT THE SYS IN PYTHON
# import sys

# emp_names = {"Name": ["kumarNallana", "prudhvi", "Rajesh", "Raja", "Bhavya"]}
# print(f"This dictionary uses {sys.getsizeof(emp_names)} bytes.")
