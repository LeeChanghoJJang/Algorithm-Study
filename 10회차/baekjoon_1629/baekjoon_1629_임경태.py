# 1629 곱셈

import sys
sys.stdin = open('input.txt')

A, B, C = map(int, input().split())
def power(A, B, C):
    if B == 1: return A % C
    elif B % 2: return A * power(A, B-1, C) % C
    else: return power(A, B//2, C)**2 % C
print(power(A, B, C))