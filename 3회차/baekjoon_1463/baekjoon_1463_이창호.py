import sys
sys.stdin = open('input.txt')
N = int(input())
DP = [0] * (N+1)
for i in range(2,N+1):
    # 기본적으로 가장 최악의 경우일때는 이전단계보다 1씩 증가함
    DP[i] = DP[i-1]+1
    # 2으로 나눠지면 이전단계보다 2 곱했던것과 현재의 값(1씩증가시킨거)랑 비교
    if i%2 ==0:
        DP[i] = min(DP[i],DP[i//2]+1)
    # 3으로 나눠지면 이전단계보다 3 곱했던것과 이전 값(2나눠진것과 1씩 증가시킨것 미니멈) 비교
    if i%3 ==0:
        DP[i] = min(DP[i],DP[i//3]+1)
print(DP[N])

