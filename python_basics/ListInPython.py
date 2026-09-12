# list_of_ids = [102, 203, 508, 404, 567, 808, 909, 101]

# list indexing
# print(list_of_ids[-1])
# print(list_of_ids[0])
# print(list_of_ids[4])
# print(list_of_ids[7])

# ids = [102, 203, 508, 404, 567, 808, 909, 101, 102, 888, 404, 102]
# new_ids = [1001, 2002, 3003, 4004, 5005]

# adding list
# ids.append(505)
# print(ids)

# ids.insert(0, 111)
# print(ids)

# print(ids.count(102))

# print(ids.index(567))
# print(ids.index(404, 0, 12))

# ids.extend(new_ids)
# print(ids)

# ids.reverse()
# print(ids)

# # DELETING A LIST
# print(ids.pop(2))
# print(ids.pop(-2))
# print(2002 in ids)
# ids.remove(2002)
# del ids[0:5]
# print(ids)
# print(ids)
# # ids.clear()
# # print(ids)
# # print(new_ids)
# ids.reverse()
# print(ids)
# ids.sort()
# print(ids)

# mathematical operations
# print(max(ids))
# print(min(ids))
# print(sum(ids))


# Slicing (List,Tuple And String)
# ids = [102, 203, 508, 404, 567, 808, 909, 101, 102, 888, 404, 102]

# slicing_ids = ids[2:]
# slicing_ids2 = ids[2: 8]
# slicing_ids3 = ids[10:2:-2]
# slicing_ids3 = ids[10:2:-1]

# print(slicing_ids)
# print(slicing_ids2)
# print(slicing_ids3)

ids = (102, 203, 508, 404, 567, 808, 909, 101, 102, 888, 404, 102)

ids2 = ids[:]

string = "KUmar nallana"
string2 = string[:]

ids3 = [102, 203, 508, 404, 567, 808, 909, 101, 102, 888, 404, 102]
ids4 = ids3[:]

print(string is string2)

print(ids is ids2)
print(ids is ids2)

print(ids3 is ids4)
