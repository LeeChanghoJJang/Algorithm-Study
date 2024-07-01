import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
depress = list(map(int,input().split()))

if sum(depress) >= M:
    exit(print(0))
dp = [0] * 1001
for i in range(1,1001):
    dp[i] =dp[i-1] + i**2

leaves = M - sum(depress) - N
quotient = leaves // (N+1)
remainder = leaves % (N+1)
result = [quotient] * (N+1)
for i in range(remainder):
    result[i]+=1

print(sum(map(lambda x:dp[x],result)))
