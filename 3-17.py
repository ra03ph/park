def sum_of_divisors(n):
    """주어진 수 n의 약수의 합을 반환하는 함수."""
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total

def find_amicable_numbers(limit):
    """주어진 범위 내의 모든 친화수를 찾는 함수."""
    amicable_pairs = []
    for num in range(1, limit + 1):
        partner = sum_of_divisors(num)
        if partner > num and partner <= limit:
            if num == sum_of_divisors(partner):
                amicable_pairs.append((num, partner))
    return amicable_pairs

# 20,000까지의 친화수 찾기
amicable_numbers = find_amicable_numbers(20000)

# 결과 출력
for pair in amicable_numbers:
    print(f"{pair[0]}의 친화수 {pair[1]}")
