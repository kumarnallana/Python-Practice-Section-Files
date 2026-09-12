# IF-ELSE STATEMENT

user_input = int(input("Enter a number bro?").strip())

# if (user_input % 2 == 0):
#     print(user_input, " is a Even Num")
# else:
#     print(user_input, " is a Odd Num")

if (user_input > 0):
    print(user_input, "is a Positive number")
    if (user_input % 2 == 0):
        print(user_input, "is a Even positive num")
    else:
        print(user_input, "is a Odd positive num")
elif (user_input < 0):
    print(user_input, "is a negative number")
    if (user_input % 2 == 0):
        print(user_input, "is a Even negative num")
    else:
        print(user_input, "is a Odd negative num")
else:
    print(user_input, "is a not a valid num")
