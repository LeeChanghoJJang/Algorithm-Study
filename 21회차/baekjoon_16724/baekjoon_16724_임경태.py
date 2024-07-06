# 16724 피리 부는 사나이
dr = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
N, M = map(int, input().split())
board = [input() for _ in range(N)]
visit = [[0] * M for _ in range(N)]
ans = 0

def check(ci, cj):
    stack = [(ci, cj)]

    while stack:
        i, j = stack[-1]

        if not visit[i][j]:
            visit[i][j] = 1
            ni, nj = i + dr[board[i][j]][0], j + dr[board[i][j]][1]
            
            if not visit[ni][nj]:
                stack.append((ni, nj))

            if visit[ni][nj] == 1:
                while stack:
                    i, j = stack.pop()
                    visit[i][j] = 2
                return True

        elif visit[i][j] == 1:
            visit[i][j] = 2
            stack.pop()

    return False

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            if check(i, j):
                ans += 1

print(ans)