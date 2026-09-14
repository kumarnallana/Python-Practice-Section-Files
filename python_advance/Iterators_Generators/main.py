employees: list[dict[str, str | int]] = [
    {"id": 1, "name": "Arjun", "score": 88},
    {"id": 2, "name": "Meera", "score": 92},
    {"id": 3, "name": "Rahul", "score": 76},
    {"id": 4, "name": "Priya", "score": 95},
    {"id": 5, "name": "Kiran", "score": 81},
]

def yield_generator(emp_data: list[dict[str, str | int]], threshold: int):
    for employee in emp_data:
        if employee["score"] > threshold:
            yield employee


emp_scores = list(yield_generator(emp_data=employees, threshold=200))

if not emp_scores:
    print("No Employees Found!")
else:
    print(emp_scores)
