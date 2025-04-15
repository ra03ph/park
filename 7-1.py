def my_greet():
    print("환영합니다.")

my_greet()
my_greet()

def inch2cm(inch):
    return inch * 2.54

for i in range(1, 6):
    cm = inch2cm(i)
    print(f"{i} 인치 = {cm:.2f} 센티미터")

def mean_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

nums = input("정수를 여러 개 입력하세요 : ").split()

nums = list(map(int, nums))

print(f"평균값은 {mean_of_n(nums):.1f}")
print(f"최댓값은 {max_of_n(nums)}")
print(f"최솟값은 {min_of_n(nums)}")       
