import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n, k = map(int, input().split())
    ls = list(map(int, input().split()))

    num = [i for i in range(n)]
    comb = list(combinations(num, k))

    result = 0

    for i in comb:
        total = 0
        for j in i:
            total += ls[j]

        if result < total:
            result = total

    print(result)
