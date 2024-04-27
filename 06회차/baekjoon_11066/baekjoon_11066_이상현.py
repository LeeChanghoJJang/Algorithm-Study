# Python, PyPy3 시간초과
# C++은 통과 ㅠ

# 백준 11066번 파일 합치기

import sys
input = sys.stdin.readline

def chk(start, end):
    if dp[start][end] != -1:
        return dp[start][end]

    if start == end:
        return 0

    min_ = float('inf')
    sum_ = sum(num_list[start:end + 1])

    for i in range(start, end):
        temp = chk(start, i) + chk(i + 1, end) + sum_

        min_ = min(min_, temp)
        dp[start][end] = min_

    return min_

T = int(input())

for _ in range(T):
    K = int(input())
    num_list = list(map(int, input().split()))
    dp = [[-1] * (K + 1) for i in range(K + 1)]

    print(chk(0, K - 1))