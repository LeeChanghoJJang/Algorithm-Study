# 1799 비숍
'''
기존 백트래킹 -> 모든 칸이 1일 때 O(2^(N^2))
핵심 : 우상향 대각선당 비숍이 놓일 때 마다, 그 좌표에 해당하는 우하향 대각선을 체크 (이분매칭)
'''

def BT(k, cnt):
    global ans
    # 마지막 대각선에 다다르면 종료
    if k == 2*N-1:
        ans = max(ans, cnt); return

    # 가지치기
    if ans >= (cnt + (2*N-k)//2): return

    # 가능한 부분 순회
    for i, j in open[k]:
        # 착수 후 다음 대각선 탐색
        if not diag[i-j]:
            diag[i-j] = True
            BT(k+2, cnt+1)
            diag[i-j] = False

    # 미착수 후 다음 대각선 탐색
    BT(k+2, cnt)

N = int(input())
grid=[list(map(int, input().split())) for _ in range(N)]
diag = [False] * (2*N-1)

# 착수 가능한 부분 저장
open = [[] for _ in range(2*N-1)]
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            open[i+j].append([i, j])

# 홀수번째 대각선과 짝수번째 대각선을 분리하여 백트래킹 진행
ans = 0
BT(0, 0)
BT(1, ans)
print(ans)