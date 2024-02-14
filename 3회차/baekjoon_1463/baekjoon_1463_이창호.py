import sys
sys.stdin = open('input.txt')
# 첫번째 방법
N = int(input())
DP = [0] * (N+1)
for i in range(2,N+1):
    DP[i] = DP[i-1]+1
    # 2로 나누어지면 2로 나눈것의 DP와 원래 코스의 DP와 비교
    if i%2 ==0:
        DP[i] = min(DP[i],DP[i//2]+1)
    if i%3 ==0:
        DP[i] = min(DP[i],DP[i//3]+1)
print(DP[N])

