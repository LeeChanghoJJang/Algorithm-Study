import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
p =list(map(int,input().split()))
q =list(map(int,input().split()))
d = int(input())

dp = [0] * 101

now = 0
for i in range(n):
    now += p[i] * q[i]
    p[i] = min(d,p[i])

for i in range(n):
    while p[i] > 0 :
        p[i]-=1
        for j in range(d,-1,-1):
            for k in range(i+1,n):
                if k + i - j <= d:
                    dp[k + i - j] = max(dp[k + i - j], dp[j] + q[k] - q[i])
print(dp[d] + r)
