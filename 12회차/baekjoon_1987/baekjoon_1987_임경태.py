# 1987 알파벳

go = ((0, 1), (1, 0), (0, -1), (-1, 0))
R, C = map(int, input().split())
board = [input() for _ in range(R)]
visit = [0] * 26
ans = 0

def DFS(i, j, cnt, visit):
    global ans
    ans = max(ans, cnt)

    for di, dj in go:
        ni = i + di
        nj = j + dj

        if not (0 <= ni < R and 0 <= nj < C): continue
        num = ord(board[ni][nj]) - 65

        if not visit[num]:
            visit[num] = 1
            DFS(ni, nj, cnt+1, visit)
            visit[num] = 0

visit[ord(board[0][0])-65]=1
DFS(0, 0, 1, visit)
print(ans)