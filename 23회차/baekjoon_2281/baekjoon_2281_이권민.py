import sys
input = sys.stdin.readline
n,m = map(int, input().split())
# M을 넘지 않는 선에서 합의 조합들. 앞에서 부터
lst =[int(input()) for _ in range(n)]
max_n = m*m*n
dp = [max_n]*(n+1)
dp[n] = 0

def note(index):
    if dp[index]!= max_n:
        return dp[index]
    
    remain = m-lst[index]
    
    for i in range(index+1,n+1):
        if remain >= 0:
            if i == n:
                dp[index] = 0
                break
            dp[index] = min(dp[index], remain*remain + note(i))
            remain -= lst[i] +1
    return dp[index]

print(note(0))

# 개같이 어렵네


    
