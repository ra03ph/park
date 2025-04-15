from datetime import date, timedelta

start_date = date(2019, 2, 14)

today = date.today()

days_passed = (today - start_date).days

print(f"춘향이와 몽룡이의 연애 시작일 : {start_date.year}년 {start_date.month}월 {start_date.day}일")
print(f"연애 시작일로부터 경과한 날짜 : {days_passed}일\n")

for days in [100, 200, 500, 1000]:
    anniv = start_date + timedelta(days=days)
    print(f"{days}일 기념일 : {anniv.year}년 {anniv.month}월 {anniv.day}일")



import math

for deg in range(0, 181, 10):
    rad = math.radians(deg)  
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    tan_val = math.tan(rad)

    print(f"sin({deg:3}) = {sin_val:6.3f}, cos({deg:3}) = {cos_val:6.3f}, tan({deg:3}) = {tan_val:6.3f}")




import random

answer = random.randint(1, 20)
attempts = 0

while True:
    try:
        guess = int(input("1~20까지의 숫자를 입력하세요: "))
        attempts += 1

        if guess < answer:
            print(f"{guess} 보다 작습니다!")
        elif guess > answer:
            print(f"{guess} 보다 큽니다!")
        else:
            print("정답입니다!")
            
            if attempts <= 3:
                print(f"{attempts}번 만에 맞춘 당신은 천재!")
            elif attempts <= 6:
                print(f"{attempts}번 만에 맞추셨네요. 잘했어요^^")
            else:
                print(f"{attempts}번 만에 맞추다니 쩝...")
            break
    except ValueError:
        print("숫자만 입력해주세요!")
