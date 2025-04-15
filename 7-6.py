try:
    a, b = input('두 수를 입력하세요 : ').split()
    result = int(a) * int(b)
except ValueError:
    print("입력 오류가 발생했습니다. 두 개의 숫자를 정확히 입력하세요.")
else:
    print("결과는 :", result)



try:
    a, b = input('두 수를 입력하세요 : ').split()
    result = int(a) * int(b)
except ValueError:
    print("숫자 두 개를 정확히 입력하세요.")
else:
    print("결과는 :", result)



a_list = [200, 300, 400]
print('a_list :', a_list)

try:
    idx = int(input('선택할 인덱스를 입력하세요 (0,1,2) : '))
    result = a_list[idx]
except ValueError:
    print("정수를 입력하세요.")
except IndexError:
    print("0, 1, 2 중 하나만 입력하세요.")
else:
    print("결과 :", result)
