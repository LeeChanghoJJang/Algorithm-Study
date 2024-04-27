import sys
sys.stdin = open('input.txt')
str1, str2 = input(), input()
N = len(str1)
M = len(str2)
# 2차원 DP에 길이가 얼마나 같은지 여부를 저장 
DP = [[0] * (M+1) for _ in range(N+1)]
# 모든 행과열 순회 
for i in range(N):
    for j in range(M):
        # 두 문자열이 같은 경우가 생기면
        if str1[i] == str2[j]:
            # 대각선에 있는 것들은 많이 차이나야 1개 차이남
            # 즉 마지막 두 문자가 같으면 늘어나는 길이도 1개라는 거임 
            DP[i+1][j+1] = DP[i][j]+1
        else:
            DP[i+1][j+1] = max(DP[i+1][j],DP[i][j+1])
print(DP[-1][-1])
