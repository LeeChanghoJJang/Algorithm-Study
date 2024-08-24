import sys
# input = sys.stdin.readline

def check(w1, w2, l):
    cnt = 0
    for i in range(l):
        if w1[i] != w2[i]:
            cnt += 1
    return cnt

s = ' '+input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

dp = [[1000]*(len(s)) for _ in range(len(s))]
dp[0][0] = 0

for i in range(1,len(s)+1):
    if dp[i-1][0] == 1000:
        continue
    for word in words:
        l = len(word)
        if sorted(s[i:i+l]) == sorted(word):
            dp[i][i+l-1] = min(dp[i][i+l-1], dp[i-1][0]+check(s[i:i+l], word, l))
            dp[i+l-1][0] = min(dp[i+l-1][0], dp[i][i+l-1])

if dp[-1][0] != 1000:
    print(dp[-1][0])
else: print(-1)