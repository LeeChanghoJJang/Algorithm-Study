import sys
sys.stdin = open('input.txt')

def backtracking(start, result):
    if len(result) == M:
        temp.add(tuple(result.copy()))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result.append(arr[i])
            backtracking(start + 1, result)
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [0] * (N + 1)
temp = set()
backtracking(0, [])
for i in sorted(temp):
    print(*i)