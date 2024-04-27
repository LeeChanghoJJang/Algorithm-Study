# 12173 금화모으기
import sys
sys.stdin = open('input.txt')
from pprint import pprint
# DP랑 비슷한 방법으로 풂
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 각 위치에 모은 금화의 높은 값을 저장하기 위한 행렬 arr_sum
    arr_sum = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,M+1):
            arr_sum[i][j] = max(arr_sum[i-1][j],arr_sum[i][j-1]) + arr[i-1][j-1]
    print(f'#{tc} {arr_sum[N][M]}')