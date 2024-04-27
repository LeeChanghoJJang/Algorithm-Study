import sys
input = sys.stdin.readline

def dfs(vertex, visited):
    if visited == (1 << N) - 1:
        if list_[vertex][0]:
            return list_[vertex][0]
        else:
            return float('inf')

    if dp[vertex][visited]:
        return dp[vertex][visited]

    min_ = float('inf')
    for i in range(1, N):
        if visited & (1 << i) or not list_[vertex][i]:
            continue

        min_ = min(min_, list_[vertex][i] + dfs(i, visited | (1 << i)))

    dp[vertex][visited] = min_
    return min_

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
print(dfs(0, 1))