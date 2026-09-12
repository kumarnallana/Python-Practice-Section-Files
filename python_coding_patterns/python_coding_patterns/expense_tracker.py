from functools import reduce

name: str = input("Tell Me Your name?")

salary: int = int(input(f"{name}, Tell me your monthly salary: "))


expenses: dict[str, int] = {
    # Housing & Utilities
    "rent": 12_000,
    "electricity": 1_800,
    "water": 400,
    "internet": 1_000,
    "mobile_recharge": 600,

    # Food & Household
    "groceries": 6_500,
    "dining_out": 3_000,

    # Travel & Commute
    "fuel_or_transport": 3_500,

    # Entertainment & Subscriptions
    "streaming_services": 800,
    "gym_membership": 1_500,

    # Health & Personal Care
    "medicines": 1_000,
    "personal_care": 1_500,

    # Miscellaneous / Buffer
    "shopping": 2_500,
    "emergency_buffer": 2_000,
}


class SalaryExpenseTracker:

    def __init__(self, salary, expenses):
        self.salary = salary
        self.expenses = expenses

    def total_expenses(self):
        values = expenses.values()

        try:
            result = reduce(lambda acc, item: acc + item, values, 1)
        except Exception as e:
            print(f"Something Went Wrong: {e}")

        return result

    def reaminning_salary(self):

        if salary < 0 and total_expenses < 0:
            return "Salary should be a valid positive number"

        total_expenses = self.total_expenses()

        final_result = salary - total_expenses

        return final_result


def print_result() -> str:
    tracker = SalaryExpenseTracker(salary=salary, expenses=expenses)

    total = tracker.total_expenses()
    remaining = tracker.reaminning_salary()

    # Format each expense item with clean spacing
    formatted_items = "\n".join(
        f"  - {k.replace('_', ' ').title():<22} : {v:>10,}"
        for k, v in expenses.items()
    )

    border = "=" * 50
    divider = "-" * 50

    report = (
        f"\n{border}\n"
        f"              MONTHLY FINANCIAL REPORT\n"
        f"                 EXPENSE BREAKDOWN\n"
        f"{divider}\n"
        f"{formatted_items}\n"
        f"{divider}\n"
        f"  Monthly Salary      : {salary:>15,}\n"
        f"  Total Expenses      : {total:>15,}\n"
        f"  Remaining Balance   : {remaining:>15,}\n"
        f"{border}\n"
    )

    return report


print(print_result())
