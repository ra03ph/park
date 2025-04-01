def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

n = int(input("숫자를 입력하세요: "))
result = sum_of_squares(n)
print(f"결과는 {result}입니다.")
