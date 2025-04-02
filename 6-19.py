s_list = ['abc', 'bcd', 'abc', 'abba', 'cdcc', 'opq', 'opq']

new_s_list = ['abc', 'bcd', 'abba', 'cdcc', 'opq']

for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)

print("new_s_list =", new_s_list)
