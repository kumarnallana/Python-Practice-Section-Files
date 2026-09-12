# class Caliculations:
#     @staticmethod
#     def ensure_larger_first(func):
#         def wrap(a, b):
#             if a < b:
#                 a, b = b, a
#             return func(a, b)
#         return wrap

#     @staticmethod
#     def log_result(func):
#         def wrap(a, b):
#             print(f"values is {a} and {b}")
#             result = func(a,  b)
#             print(f'Final Result  = {result}')
#             return result
#         return wrap


# @Caliculations.ensure_larger_first
# @Caliculations.log_result
# def substract_func(a, b):
#     return a - b


# @Caliculations.log_result
# def divide_func(a, b):
#     return a/b


# sum_total = divide_func(3, 4)
# print("------------------------------------------------------")

# divide_total = substract_func(10, 4)

# print(sum_total)
# print("------------------------------------------------------")
# print(divide_total)


def timer_decorator(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper


@timer_decorator
def calculate_sum(n):
    return sum(range(n))


print("Total:", calculate_sum(100))
