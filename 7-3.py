s1 = 'Kang Young Min'
s2 = 'Kang Young-Min'
s3 = 'Park Dong Min'
s4 = 'Park Dong-Yun'

names = [s1, s2, s3, s4]

modified_names = []

for name in names:
    new_name = name.replace(' ', '').replace('-', '').upper()
    print(f"{name}(은)는 {new_name}(으)로 수정됨")
    modified_names.append(new_name)

print()  

for name in modified_names:
    count = name.count('N')
    print(f"{name} : {count} 개의 N이 나타남")

    

price = {'김밥': 5000, '어묵': 3000, '떡볶이': 2000}

print(price['김밥'])  

print(price)  

print(price.values())  

print(price.keys())  

print("이 식당의 메뉴 개수는", len(price), "개 입니다.")



t = (10, 20, 30, 40)

print(t[0])       

print(t[0:2])     

print(t[1:])      

print(t[:3])      

print(t[1::2])    

print(t[::-1])

tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)




result = []
for item in tup:
    if item not in result:
        result.append(item)

result_tuple = tuple(result)

print("중복 제거 튜플:", result_tuple)




lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

n = len(lst)
for i in range(n - 1):  
    for j in range(n - 1 - i):  
        if lst[j] > lst[j + 1]:  
            lst[j], lst[j + 1] = lst[j + 1], lst[j]  

print("정렬된 결과는 =", lst)



population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_B = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

vote_A = sum(population_A[2:])
vote_B = sum(population_B[2:])

print("마을 A와 B에 보낼 투표용지의 개수는 각각", vote_A, "장과", vote_B, "장입니다.")



import re

def is_palindrome(s):
    s = re.sub(r'[^a-z0-9]', '', s.lower())

    return s == s[::-1]

text = input("문자열을 입력하시오 : ")

if is_palindrome(text):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
