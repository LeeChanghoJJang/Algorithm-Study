import sys
sys.stdin = open('input.txt')
# 첫번째 도전 : 시간초과
N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    max_sum = 0
    for x in range(x1-1,x2):
        max_sum += sum(arr[x][y1-1:y2])
    print(max_sum)

# 두번째 도전 : DP 이용
import sys
N,M = map(int,sys.stdin.readline().split())

DP = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
DP_sum = [[0]*(N+1) for _ in range(N+1)]

for row in range(1,N+1):
    for col in range(1,N+1):
        DP_sum[row][col] = DP_sum[row-1][col] + DP_sum[row][col-1] - DP_sum[row-1][col-1] + DP[row-1][col-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(DP_sum[x2][y2] - DP_sum[x1-1][y2] - DP_sum[x2][y1-1] + DP_sum[x1-1][y1-1])