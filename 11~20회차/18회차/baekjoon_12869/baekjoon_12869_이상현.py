import sys
sys.stdin = open('input.txt')

from itertools import permutations

ps = list(permutations([9, 3, 1]))

def muli(s, c, v, cnt):
    global min_, dp, ps

    s, c, v = max(s, 0), max(c, 0), max(v, 0)

    if s <= 0 and c <= 0 and v <= 0:
        min_ = min(min_, cnt)
        return

    if dp[s][c][v] <= cnt and dp[s][c][v]:
        return

    dp[s][c][v] = cnt

    for p in ps:
        muli(s - p[0], c - p[1], v - p[2], cnt + 1)

N = int(input())
list_ = list(map(int, input().split()))
dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]
min_ = float('inf')
muli(*list_[:3], 0)

print(min_)