import sys
input = sys.stdin.readline


def solve(N, v):
    v.sort()
    
    total = sum(i for _, i in v)
    mid = total / 2

    cur = 0
    for pos, tmp in v:
        cur += tmp
        if cur >= mid:
            return pos


N = int(input())
v = [list(map(int, input().split())) for _ in range(N)]

result = solve(N, v)
print(result)
