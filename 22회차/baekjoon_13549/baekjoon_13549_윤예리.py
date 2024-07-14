import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
dp = [0] * 100001

def bfs(x, y):
    q = deque()

    if x == 0:
        q.append(1)
    else:
        q.append(x)

    while q:
        x = q.popleft()

        if y == x:
            return dp[x]

        for nx in (x-1, x+1, x*2):
            if 0 <= nx < 100001 and not dp[nx]:
                if nx == 2 * x:
                    dp[nx] = dp[x]
                    q.appendleft(nx)
                else:
                    dp[nx] = dp[x] + 1
                    q.append(nx)

if n == 0:
    if k == 0: print(0)
    else: print(bfs(n, k) + 1)
else:
    print(bfs(n, k))


#  왜 안됨? 진짜 모름
# for i in range(n, k+1):
#     if i%n == 0: dp[i] = 0
#     else:
#         dp[i] = min(dp[i//2], dp[i-1] + 1, dp[i+1] + 1)
#
# print(dp[k])