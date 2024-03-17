import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
inf = int(1e9)
min_val = int(1e9)
for i in range(3):
    # 디폴트를 큰값으로 저장
    DP = [[inf] * 3 for _ in range(N)]
    # 첫행 기본값 저장  
    DP[0][i] = arr[0][i]
    # 맨처음 주어진 값이 i번째 값일 때 DP 돌린다
    for j in range(1,N):
        DP[j][0] = arr[j][0] + min(DP[j - 1][1], DP[j - 1][2])
        DP[j][1] = arr[j][1] + min(DP[j - 1][0], DP[j - 1][2])
        DP[j][2] = arr[j][2] + min(DP[j - 1][0], DP[j - 1][1])
    # 맨 처음 주어진 값과 같지 않는 열에 해당할 때 최소값을 저장 
    for k in range(3):
        if i != k:
            min_val = min(min_val, DP[-1][k])
print(min_val)
