# 2667 단지 번호 붙이기

def DFS(arr, i, j, cnt):
    S = [[i, j]]
    while S:
        i, j = S.pop()

        for di, dj in go:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj]:
                arr[ni][nj] = 0; cnt += 1; S.append([ni, nj])
    return cnt

n, ans = int(input()), []
go = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            arr[i][j] = 0
            ans.append(DFS(arr, i, j, 1))

print(len(ans))
for i in sorted(ans): print(i)