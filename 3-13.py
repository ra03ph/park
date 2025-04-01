def is_armstrong(number):
    # 각 자리수를 리스트로 변환
    digits = [int(d) for d in str(number)]
    # 자리수의 개수
    power = len(digits)
    # 각 자리수를 거듭 제곱하여 합산
    return sum(d ** power for d in digits) == number

# 세 자리 암스트롱 수 찾기
armstrong_numbers = []
for num in range(100, 1000):
    if is_armstrong(num):
        armstrong_numbers.append(num)

print("세 자리 암스트롱 수:", armstrong_numbers)
