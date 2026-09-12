# STRINGS IN PYTHON
# print(ord("a"))
# print(ord("Z"))
# print(chr(97))
# print(chr(122))

# INDEXING IN STRINGS
# string = "kumar nallana"
# print(string[0])
# print(string[-4])
# print(string[2])
# print(string[-1])

# STRINGS ARE IMMUTABLE
# string = "kumar"
# string[0] = "m"
# print(string)

# output will be :-
"""   string[0] = "m"
    ~~~~~~^^^
TypeError: 'str' object does not support item assignment"""

# MULTIPLE LINES STRING
# string_eg = """
# -----------------
# Name: "kumar",
# age: 21,
# gender: male,
# ----------------
# """

# print(string_eg)


# Escape Sequences and Raw Strings

# s1 = "C:\\project\\name.py"
# s2 = R"C:\project\name.py"  # R or r => is a built Raw string in python
# print(s1)
# print(s2)

# string_eg = "hi, \n im kumar nallana \t byee byee..!"

# print(string_eg)

# F- STRING IN PYTHON
# x = 10
# y = 20

# print(f"x + y = {x + y}")
# print(f"x * y = {x * y}")
# print(f"x // y = {x // y}")
# print((f"x ** y = {x ** y}"))

# UPPERCASE AND LOWERCASE IN PYTHON
# user = "Kumar nallana"

# print(f"Your name in UPPERCASE = {user.upper()}")
# print(f"Your name in lowercase = {user.lower()}")


# OPERATIONS ON STRINGS (PART -1 )
# frst_str = "Tony Stark is iron man and Tony Stark is iron man"
# second_str = "Tony Stark is iron man"

# print(second_str in frst_str)
# print(second_str not in frst_str)

# print(frst_str.index(second_str))
# print(frst_str.index(second_str))
# print(frst_str.startswith("Tony"))
# print(second_str.endswith("Tony"))
# print(second_str.endswith("Tony"))

# SPLIT AND JOIN
# str_spliting = frst_str.split()
# str_joining = "||".join(str_spliting)
# print(str_joining)


# demo_str = "--- -ku m a r_n a @@  l l  a  @@ na------"

# makeTranslate = str.maketrans("", "", " @-")
# result = demo_str.translate(makeTranslate)

# print(result)
# print(demo_str.strip("-"))
# print(demo_str.lstrip("-"))
# print(demo_str.rstrip("-"))
# print(demo_str.strip())

# print(demo_str.find("kumar"))
# print(demo_str.find(demo2_str))
# print(demo2_str.find(demo_str))


# COMPARASION IN STRINGS
# s1 = "z"
# s2 = "abcdefg"
# print(s1 > s2)
# print(s1 < s2)
# print(s1 >= s2)
# print(s1 <= s2)
# print(s1 != s2)
# print(s1 == s2)


# RE-PRACTICING STRINGS
# x = 50
# y = 35
# print(f"x - y = {x - y}")

# frst_str = "Tony Stark is iron man and Tony Stark is iron man"
# second_str = "Tony Stark is iron man"

# print(frst_str.index(second_str))

# print(frst_str[-1:-10:-4])

# text = "#"
# multiple = text * 30

# print(text.isdigit())
# print(text.isalpha())
# print(text.isalnum())

# for char in multiple:
#     print(char)

# print(len(multiple))
