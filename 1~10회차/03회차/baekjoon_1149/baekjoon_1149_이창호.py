# 1149 RGB 거리
import sys
sys.stdin = open('input.txt')
N = int(input())
'''
집의 특성상 이전 단계의 색만 이후 단계의 색에 영향을 미침
아래의 6가지 경우가 반복되는 양상 => 각 위치에 이전단계의 경우에 따른 min값을 저장시킨다.
현재     이전단계  
빨강 + (노랑, 초록)
노랑 + (빨강, 초록)
파랑 + (빨강, 노랑) 
'''
DP = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
    # 현 : 빨강 + 이전 : min(초록,노랑)
    DP[i][0] = min(DP[i - 1][1],DP[i - 1][2]) + DP[i][0]
    # 현 : 초록 + 이전 : min(빨강,노랑)
    DP[i][1] = min(DP[i - 1][0],DP[i - 1][2]) + DP[i][1]
    # 현 : 노랑 + 이전 : min(빨강,초록)
    DP[i][2] = min(DP[i - 1][0],DP[i - 1][1]) + DP[i][2]
print(min(DP[N-1]))
