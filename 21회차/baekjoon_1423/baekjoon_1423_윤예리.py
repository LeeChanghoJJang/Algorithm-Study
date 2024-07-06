import sys
input = sys.stdin.readline

n = int(input())
chars = list(map(int, input().split()))
power = list(map(int, input().split()))
d = int(input())

def solution(idx1, idx2, idx3):
    if idx2 == n-1:
        return 0

    tmp = dp[idx1][idx2][idx3]
    if tmp != -1:
        return tmp

    tmp = 0
    for i in range(idx3 + chars[idx2]):
        if idx1 < i:
            break
        tmp = max(tmp, solution(idx1-1, idx2+1, i) + (power[idx2+1] - power[idx2]) * i)

    return tmp

dp = [[[0] * 105 for _ in range(n+1)] for _ in range(105)]
r = 0
for i in range(n):
    r += power[i] * power[i]

print(r + solution(d, 0, 0))
