import math
import sys

input = sys.stdin.readline
n = int(input())


# 소수 판별 함수
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


# n자리 소수를 생성하는 함수
def generate_primes(n):
    if n == 1:
        return [2, 3, 5, 7]

    smaller_primes = generate_primes(n - 1)
    new_primes = []
    for prime in smaller_primes:
        for digit in '1379':  # 마지막 자리에는 짝수가 올 수 없음
            candidate = prime * 10 + int(digit)
            if is_prime(candidate):
                new_primes.append(candidate)
    return new_primes


result = generate_primes(n)

for prime in sorted(result):
    print(prime)
