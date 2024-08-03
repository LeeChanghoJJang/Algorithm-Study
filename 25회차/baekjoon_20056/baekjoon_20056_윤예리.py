import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireball = deque([])
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1, c-1, m, s, d])

arr = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(K):

    while fireball:
        cr, cc, cm, cs, cd = fireball.popleft()
        nr = (cr + cs * dr[cd]) % N
        nc = (cc + cs * dc[cd]) % N
        arr[nr][nc].append([cm, cs, cd])

    for r in range(N):
        for c in range(N):
            if len(arr[r][c]) > 1: # 2개 이상이다?
                m_total, s_total, odd, even, cnt = 0, 0, 0, 0, len(arr[r][c])
                while arr[r][c]:
                    m, s, d = arr[r][c].pop(0)
                    m_total += m
                    s_total += s

                    if d % 2: odd += 1
                    else: even += 1

                if odd == cnt or even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                if m_total//5:
                    for d in nd:
                        fireball.append([r, c, m_total//5, s_total//cnt, d])

            if len(arr[r][c]) == 1:
                fireball.append([r, c] + arr[r][c].pop())

print(sum([f[2] for f in fireball]))
