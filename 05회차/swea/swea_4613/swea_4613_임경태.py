import sys
sys.stdin = open('input.txt')

def comb(row, col, cnt):
    # 최종 행과 열까지 도달해야 최솟값 비교
    if row == N and col == 3:
        global min_cnt
        min_cnt = min(min_cnt, cnt)
        return

    # 최종 행 또는 열까지 도달하지 못한 경우 다음 비교
    if row < N and col <= 2:
        color = old_flag[row][col]
        comb(row+1, col, cnt + M - color)   # 색 안바꿈
        comb(row+1, col+1, cnt + M - color) # 색 바꿈

for tc in range(int(input())):
    N, M = map(int, input().split())

    # 오래된 깃발 행마다 색깔 개수 입력
    old_flag = []
    for _ in range(N):
        row = input()
        old_flag.append((row.count('W'), row.count('B'), row.count('R')))

    min_cnt = N * M
    comb(0, 0, 0)
    print(f'#{tc+1}', min_cnt)