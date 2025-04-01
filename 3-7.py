def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input("숫자를 입력하세요: "))
if is_prime(n):
    print(f"{n}는 소수입니다.")
else:
    print(f"{n}는 소수가 아닙니다.")
