import sys
sys.stdin = open('input.txt')

N= int(input())
# 맨 처음 1부터 9까지는 1자리는 연속된다고 가정하고 시작
DP =  [[0] +[1]* 9] + [[0] * 10 for _ in range(N-1)]
# 열 우선순회하여 연속된 정도를 저장
for i in range(1,N):
    for j in range(10):
        # 뒷 자리수가 0이면 연속되는 경우는 1밖에 없으므로 이전의 1에 저장된 값 저장
        if j ==0:
            DP[i][0] = DP[i-1][1]
        # 9면 8밖에 없으므로
        elif j==9:
            DP[i][9] = DP[i-1][8]
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]
# 맨 마지막 행에 모든 경우의수 저장됨
print(sum(DP[N-1])%int(1e9))
