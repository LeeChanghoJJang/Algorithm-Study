import sys
input = sys.stdin.readline

dir = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0 ,1)
}

def solution(x, y, idx):
    global answer
    if visited[x][y] != -1:
        if visited[x][y] == idx:
            answer += 1
        return

    visited[x][y] = idx
    dx, dy = dir[arr[x][y]]
    solution(x+dx, y+dy, idx)


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

idx = 0
answer = 0
for i in range(n):
    for j in range(m):
        solution(i, j, idx)
        idx += 1

print(answer)
# print(visited)



