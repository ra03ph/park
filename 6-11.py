numbers = input("5개의 수를 입력하세요: ").split()

n_list = [int(num) for num in numbers]

total = sum(n_list)
average = total / len(n_list)
max_value = max(n_list)
min_value = min(n_list)

print("합:", total)
print("평균:", average)
print("최댓값:", max_value)
print("최솟값:", min_value)
