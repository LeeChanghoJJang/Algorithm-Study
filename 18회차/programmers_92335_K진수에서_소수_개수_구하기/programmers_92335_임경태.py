# 92335 k진수에서 소수 개수 구하기

def solution(n, k):
    # k진수로 변환
    new_n = ""
    while n > 0:
        new_n = str(n % k) + new_n
        n //= k
    # 0을 기준으로 분리
    nums = new_n.split('0')
    # 소수 판별 및 개수 세기
    ans = sum(is_prime(int(num)) for num in nums if num)
    return ans

def is_prime(n):
    if n <= 1: return 0
    if n == 2: return 1
    if n % 2 == 0: return 0
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return 0
    return 1