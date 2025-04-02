n_list = [10, 20, 30, 50, 60]

max_value = n_list[0]

for number in n_list:
    if number > max_value:
        max_value = number

print("리스트 원소들:", n_list)
print("리스트 원소들 중 최대값:", max_value)
