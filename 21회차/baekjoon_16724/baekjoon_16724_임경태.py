# 16724 피리 부는 사나이
dr = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
N, M = map(int, input().split())
board = [input() for _ in range(N)]
visit = [[0] * M for _ in range(N)]
ans = 0

def check(ci, cj):
    stack = [(ci, cj)]

    # (0: 방문 안함, 1: 방문 중, 2: 방문 완료)
    while stack:
        i, j = stack[-1]

        # 현재 위치가 방문되지 않은 경우
        if not visit[i][j]:
            visit[i][j] = 1
            ni, nj = i + dr[board[i][j]][0], j + dr[board[i][j]][1]

            # 다음 위치가 방문되지 않은 경우
            if not visit[ni][nj]:
                stack.append((ni, nj))

            # 다음 위치가 방문 중인 경우 (사이클 발견)
            if visit[ni][nj] == 1:
                while stack:
                    i, j = stack.pop()
                    visit[i][j] = 2
                return True

        # 현재 위치가 방문 중인 경우
        elif visit[i][j] == 1:
            visit[i][j] = 2
            stack.pop()

    return False

# 보드의 모든 위치를 순회
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            if check(i, j):
                ans += 1

print(ans)