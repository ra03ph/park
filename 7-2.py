pi = 3.14

def volume_cube(s):
    return s ** 3

def volume_cuboid(w, h, l):
    return w * h * l

def volume_cone(r, h):
    return (1/3) * pi * r**2 * h

def volume_sphere(r):
    return (4/3) * pi * r**3

def volume_cylinder(r, h):
    return pi * r**2 * h


print("(1)", volume_cube(12))   
print("(2)", volume_cube(20))                
print("(3)", volume_cuboid(3, 5, 6))          
print("(4)", volume_cone(20, 10))             
print("(5)", volume_sphere(15))              
print("(6)", volume_cylinder(20, 10)) 

def sum_range(n1, n2):
    return sum(range(n1, n2 + 1))

print("10에서 20까지의 정수의 합 : {:>5}".format(sum_range(10, 20)))
print("40에서 100까지의 정수의 합 : {:>5}".format(sum_range(40, 100)))

ssn = input("주민등록번호 첫 6자리 형식 입력: ")

year = int(ssn[:2])
month = int(ssn[2:4])
day = int(ssn[4:6])

if year >= 50:
    full_year = 1900 + year
else:
    full_year = 2000 + year

print(f"{full_year}년 {month}월 {day}일")
