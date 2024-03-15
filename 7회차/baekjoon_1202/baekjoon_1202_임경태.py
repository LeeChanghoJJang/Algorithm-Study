# 1202 보석 도둑 (골드2)

from heapq import heappush, heappop

N, K = map(int, input().split())
jwl = sorted([list(map(int, input().split())) for _ in range(N)], reverse=True)
ans, Q = 0, []

for w in sorted(int(input()) for _ in range(K)):
    while jwl and jwl[-1][0] <= w: heappush(Q, -jwl.pop()[1])
    if Q: ans -= heappop(Q)
    if not (Q or jwl): break

print(ans)

'''
106268KB / 1356ms
'''