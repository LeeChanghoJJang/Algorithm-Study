import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,list(input()))) for _ in range(N)]
    result = 0
    # 위쪽과 아래쪽 나누어 합산
    for row in range(N):
        row_sum = 0
        if row <=N//2:
            for col in range(N//2 - row, N//2 + row + 1):
                row_sum += arr[row][col]
            result += row_sum
        else:
            for col in range(row-N//2,N-(row-N//2)):
                row_sum += arr[row][col]
            result += row_sum
    print(f'#{tc} {result}')

