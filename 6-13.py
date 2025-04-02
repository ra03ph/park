import math

n = int(input("n을 입력하세요: "))

numbers = input(f"{n}개의 수를 입력하세요: ").split()

n_list = [int(num) for num in numbers]

mean = sum(n_list) / n

variance = sum((x - mean) ** 2 for x in n_list) / n
std_dev = math.sqrt(variance)

print("합:", sum(n_list))
print("평균:", mean)
print("표준편차:", std_dev)
