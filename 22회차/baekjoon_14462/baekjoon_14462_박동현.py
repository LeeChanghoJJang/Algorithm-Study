import sys
input = sys.stdin.readline


N = int(input())

left = [0]+[int(input()) for _ in range(N)]
right = [0]+[int(input()) for _ in range(N)]

DP = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        # 이을게 있는 경우
        if abs(left[i]-right[j]) <=4:
            # 이전것에서 하나 올림
            DP[i][j] = DP[i-1][j-1]+1
        # 이을게 없는 경우
        else :
            # 얘랑 이은게 있는지 보고, 최대값으로 설정
            DP[i][j] = max(DP[i-1][j],DP[i][j-1])

print(DP[-1][-1])