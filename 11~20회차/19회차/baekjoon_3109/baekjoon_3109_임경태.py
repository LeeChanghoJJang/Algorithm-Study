# 3109 빵집
go = (-1, 0, 1)
R, C = map(int, input().split())
store = [list(input()) for _ in range(R)]
ans = 0

def DFS(i, j):
    # 현재 열이 마지막 열이라면 성공 개수 증가
    if j == C-1:
        global ans
        ans += 1
        return True

    # 가능한 세 방향으로 이동 시도
    for di in go:
        ni, nj = i + di, j + 1
        if 0<=ni<R and store[ni][nj] == '.':
            store[ni][nj] = 'x'
            # 재귀적으로 다음 위치에서 파이프 설치 시도
            if DFS(ni, nj):
                return True # 설치 성공
    return False # 설치 실패

# 각 행에서 시작
for r in range(R):
    DFS(r, 0)

print(ans)