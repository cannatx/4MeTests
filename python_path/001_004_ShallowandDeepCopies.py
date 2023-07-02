import copy

old_str = "Python"

new_str = old_str

print(new_str[2])

fisr_string = "Will"
second_string = copy.copy(fisr_string)

one_string = copy.deepcopy(fisr_string)

# lists
names = ["Sara", "David", "Warner", "Sandy"]
print(f"Names:{names}")
# shallow copy
new_names = names
print(f"New_names: {new_names}")
# Deep copy
names_copycopy = copy.copy(names)

names[0] = "changed name"

print(f"Names: {names}")
print(f"new_names: {new_names}")
print(f"names_copycopy: {names_copycopy}")

# nested_lists (deep of fisrt level, shallow of second)
old_list = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
print(f"old_list: {old_list}")
new_list = copy.copy(old_list)
print(f"new_list: {new_list}")
old_list[1][1] = "five"
print(f"old_list: {old_list}")
print(f"new_list: {new_list}")

new_deep_list = copy.deepcopy(old_list)
print(f"old_list: {old_list}")
print(f"new_deep_list: {new_deep_list}")
old_list[1][2] = "Six"

print(f"old_list: {old_list}")
print(f"new_deep_list: {new_deep_list}")

##

new_shallow_list_builtin = old_list.copy()
print(f"old_list: {old_list}")
print(f"new_shallow_list_builtin: {new_shallow_list_builtin}")
old_list[2][0] = "Seven"
new_shallow_list_builtin.append([10, 11, 12])
print(f"old_list: {old_list}")
print(f"new_shallow_list_builtin: {new_shallow_list_builtin}")
