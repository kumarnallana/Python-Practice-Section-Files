"""
    Dictionary is mutable and stores data in key–value pairs; it is declared using curly braces {} with key: value format.

Most used Python dictionary methods / operations (developer usage):
get(), keys(), values(), items(), update(), pop(), popitem(), clear(), len(), Key access (dict[key]), Membership (in / not in), Iteration (for key, value in dict.items()).
    """

# DECLARING A DICTONARY
# dicto_py = {{"city": "viravada"}}
# dicto_py["name"] = "kumar"
# dicto_py["age"] = 21
# dicto_py['branch'] = "cse"
# dicto_py['std_id'] = 20371

# print(dicto_py)

d = {"name": ["kumar", "Prudhvi", "Ravi"], "age": [21, 22, 19],
     "address": {"city": "viravada", "pincode": 533450, "State": "Ap"}, "is_alive": "Not found!"}

# DESTRUCTURING A DICTONARY
# name, age, address = d.values()
# city, pincode, state = address.values()
# print(name)
# print(age)
# print(address)
# print(city)
# print(pincode)
# print(state)

# LOOPING OVER DICTONARY TO GET KEY: VALUE PAIRS
# for key, value in d.items():
#     print(f"{key}: {value}")

d.update({"branch": ["Cse", "Mech", "Ece"]})
# print(d)

# d.clear()
# print(d)

# total_address = d.pop("address")
# print(total_address)

# alive = d.pop("is_alive")
# print(alive)

# print(d)

# pop_end = d.popitem()
# print(pop_end)

# print(d)

# dic_length = len(d)
# print(dic_length)

name = d["name"][1]
print(name)

is_present = "name" in d
print(is_present)

is_not_present = "pincode" not in d
print(is_not_present)

# NESTED CHECKING
is_present_in_nested = "city" not in d["address"]
print(is_present_in_nested)  # FALSE

is_present_in_nested2 = "city" in d["address"]
print(is_present_in_nested2)  # TRUE
