print( 200,'+', 300,'+', 400 ,'=', 200 + 300 + 400 )

weight = 30
height = 60
print(weight)
print(height)

width = 30
height = 60
area = width * height
print('사각형의 면적:', area)

width = 40
height = 20
area = 0.5 * width * height
print('삼각형의 면적:', area)

side = int(input('정사각형의 밑변을 입력하시오:'))
print('정사각형의 면적:', side ** 2)

print('10에서 10까지의 합 :' + str(1+2+3+4+5+6+7+8+9+10))
print('10! =' + str(10*9*8*7*6*5*4*3*2*1))

print("a    n    a**n")
for a in range(2, 7):
    n = 2
    print(f"{a}{n}{a ** n}")

print("섭씨    화씨")
for celsius in range(0, 51, 10):
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}    {fahrenheit:.1f}")

celsius = float(input("섭씨 온도를 입력하세요 : "))
fahrenheit = (9/5) * celsius + 32
print(f"섭씨 {celsius} 도는 화씨 {fahrenheit} 도 입니다.")

fahrenheit = float(input("화씨 온도를 입력하세요 : "))
celsius = (fahrenheit - 32) * 5/9
print(f"화씨 {fahrenheit} 도는 섭씨 {celsius:.1f} 도 입니다.")

radius = 11
PI = 3.141592
circumference = 2 * PI * radius
area = PI * radius ** 2
print(f"원의 반지름 = {radius}, 원의 둘레 = {circumference:.6f}, 원의 면적 = {area:.6f}")

radius = float(input("원의 반지름을 입력하세요 : "))
PI = 3.141592
circumference = 2 * PI * radius
area = PI * radius ** 2
print(f"원의 둘레 = {circumference:.6f}, 원의 면적 = {area:.6f}")

for num in range(2, 11):
    sqrt = num ** 0.5
    print(f"{num}의 제곱근 = {sqrt}")

import math
a = int(input("밑변을 입력하세요 : "))
b = int(input("높이를 입력하세요 : "))
c = math.sqrt(a**2 + b**2)
print(f"빗변 : {c:.1f}")

z = 1 + 2j
rotation = 1j  # 90도 회전 (cos 90°=0, sin 90°=1)
result = z * rotation
print(f"회전하기 전 : {z}")
print(f"90도 회전한 후 : {result}")

result = [2 << i for i in range(10)]
print(' '.join(map(str, result)))

n = int(input("정수를 입력하세요: "))
print(f"이 수가 짝수인가요? {n % 2 == 0}")

n = int(input("정수를 입력하세요 : "))
condition = (0 <= n <= 100) and (n % 2 == 0)
print(f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? {condition}")

a = 5  # 0b101
b = 6  # 0b110
print(f"{bin(a)} & {bin(b)} = {bin(a & b)}")
print(f"{bin(a)} | {bin(b)} = {bin(a | b)}")
print(f"{bin(a)} ^ {bin(b)} = {bin(a ^ b)}")

n = int(input("정수를 입력하시오 : "))
print(f"{n} 의 2진수 값 : {bin(n)}")
print(f"{n} 의 2진수 값에 대한 비트단위 부정값 : {bin(~n)}")

a = int(input("정수 a를 입력하시오 : "))
b = int(input("정수 b를 입력하시오 : "))
print(f"a / b의 몫 : {a // b}")
print(f"a / b의 나머지 : {a % b}")

n = int(input("세 자리 정수를 입력하시오 : "))
백의자리 = n // 100
십의자리 = (n // 10) % 10
일의자리 = n % 10
print(f"백의 자리 : {백의자리}")
print(f"십의 자리 : {십의자리}")
print(f"일의 자리 : {일의자리}")

n = int(input("세 자리 정수를 입력하시오 : "))
print(n % 10)
print((n // 10) % 10)
print(n // 100)



    
=======
print(200, '+', 300, '+', 400, '=', 200 + 300 + 400)

weight = 30
height = 60
print(weight)
print(height)

width = 30
height = 60
area = width * height
print("사각형의 면적 :", area)

width = 40
height = 20
area = (width * height) // 2
print("삼각형의 면적 :", area)

side = int(input('정사각형의 밑변을 입력하시오 : '))
print("정사각형의 면적 :", side ** 2)

print("10에서 10까지의 합 : " + str(1+2+3+4+5+6+7+8+9+10))

print("10! = " + str(10*9*8*7*6*5*4*3*2*1))

print("a    n    a**n")
for a in range(2, 7):
    n = 2
    print(f"{a}{n}{a ** n}")

print("섭씨    화씨")
for celsius in range(0, 51, 10):
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}    {fahrenheit:.1f}")

celsius = float(input("섭씨 온도를 입력하세요 : "))
fahrenheit = (9/5) * celsius + 32
print(f"섭씨 {celsius} 도는 화씨 {fahrenheit} 도 입니다.")

fahrenheit = float(input("화씨 온도를 입력하세요 : "))
celsius = (fahrenheit - 32) * 5/9
print(f"화씨 {fahrenheit} 도는 섭씨 {celsius:.1f} 도 입니다.")

radius = 11
PI = 3.141592
circumference = 2 * PI * radius
area = PI * radius ** 2
print(f"원의 반지름 = {radius}, 원의 둘레 = {circumference:.6f}, 원의 면적 = {area:.6f}")

radius = float(input("원의 반지름을 입력하세요 : "))
PI = 3.141592
circumference = 2 * PI * radius
area = PI * radius ** 2
print(f"원의 둘레 = {circumference:.6f}, 원의 면적 = {area:.6f}")

for num in range(2, 11):
    sqrt = num ** 0.5
    print(f"{num}의 제곱근 = {sqrt}")

import math
a = int(input("밑변을 입력하세요 : "))
b = int(input("높이를 입력하세요 : "))
c = math.sqrt(a**2 + b**2)
print(f"빗변 : {c:.1f}")

z = 1 + 2j
rotation = 1j  # 90도 회전 (cos 90°=0, sin 90°=1)
result = z * rotation
print(f"회전하기 전 : {z}")
print(f"90도 회전한 후 : {result}")

result = [2 << i for i in range(10)]
print(' '.join(map(str, result)))

n = int(input("정수를 입력하세요: "))
print(f"이 수가 짝수인가요? {n % 2 == 0}")

n = int(input("정수를 입력하세요 : "))
condition = (0 <= n <= 100) and (n % 2 == 0)
print(f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? {condition}")

a = 5  # 0b101
b = 6  # 0b110
print(f"{bin(a)} & {bin(b)} = {bin(a & b)}")
print(f"{bin(a)} | {bin(b)} = {bin(a | b)}")
print(f"{bin(a)} ^ {bin(b)} = {bin(a ^ b)}")

n = int(input("정수를 입력하시오 : "))
print(f"{n} 의 2진수 값 : {bin(n)}")
print(f"{n} 의 2진수 값에 대한 비트단위 부정값 : {bin(~n)}")

a = int(input("정수 a를 입력하시오 : "))
b = int(input("정수 b를 입력하시오 : "))
print(f"a / b의 몫 : {a // b}")
print(f"a / b의 나머지 : {a % b}")

n = int(input("세 자리 정수를 입력하시오 : "))
백의자리 = n // 100
십의자리 = (n // 10) % 10
일의자리 = n % 10
print(f"백의 자리 : {백의자리}")
print(f"십의 자리 : {십의자리}")
print(f"일의 자리 : {일의자리}")

n = int(input("세 자리 정수를 입력하시오 : "))
print(n % 10)
print((n // 10) % 10)
print(n // 100)
