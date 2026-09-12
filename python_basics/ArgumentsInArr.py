

# def add_fun(num1, num2=20):#DEFAULT ARGUMENT
#     return num1 * num2


# user_data = add_fun(user_input)

# print(user_data)

# WE WILL TRY IT LATER

# user_input = int(input("Enter a number?"))
# user_input2 = int(input("Enter a second number?"))


# def user_items(num1, *nums):
#     product = num1
#     for loop in nums:
#         product *= loop
#     print(product)


# user_items(user_input, user_input2)

# user_name = input("Enter your name?")
# user_age = int(input("Enter your age,location,pinCode?"))


# def userDb(name, age=18):
#     checking_age = f"Name: {name} || Age: {age}" if age >= 18 else "Age Must be greather than 18"
#     return checking_age


# user_parameter = userDb(name=user_name, age=user_age)  # DEFAULT PARAMETER
# print(user_parameter)


user_name = input("Enter your name?")
user_age = input("Enter your age?")
user_location = input("Enter your Location?")
user_pincode = input("Enter your Pincode?")


def person(name, **remaining_data):
    print("Name on your order:", user_name)
    print(remaining_data)
    return "Booking Successfull 🍾✅"


person(name=user_name, user_age=user_age,
       user_location=user_location, user_pincode=user_pincode)
