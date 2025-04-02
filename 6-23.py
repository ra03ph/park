person1 = ['윤달', 20, 180.0, 100.0]
person2 = ['이사부', 25, 170.0, 70.0]
person3 = ['평강', 22, 169.0, 60.0]
person4 = ['험거세', 40, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4

def how_many_persons(person_list):
    return len(person_list) // 4

def compute_average_age(person_list):
    total_age = sum(person_list[i + 1] for i in range(0, len(person_list), 4))
    return total_age / (len(person_list) // 4)

def count_males_females(person_list):
    n_male = sum(1 for i in range(0, len(person_list), 4) if person_list[i][0] in ['윤달', '이사부', '평강', '험거세'])  # 예시로 남자를 판단
    n_female = (len(person_list) // 4) - n_male
    return n_male, n_female

def display_persons(person_list):
    for i in range(0, len(person_list), 4):
        print(person_list[i], person_list[i + 1], person_list[i + 2], person_list[i + 3])

n_persons = how_many_persons(person_list)
average_age = compute_average_age(person_list)
n_male, n_female = count_males_females(person_list)

print(f"명 정보가 {n_persons}명 있습니다.")
print(f"평균 나이는 {average_age:.2f}세입니다.")
print(f"리스트에는 남자 {n_male}명, 여자 {n_female}명입니다.")

display_persons(person_list)
