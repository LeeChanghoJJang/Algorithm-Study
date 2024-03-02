# 행: h, 열: w
w, h = map(int, input().split())
# arr = [[0] * w for _ in range(h)]

p, q = map(int, input().split())
t = int(input())

tp = (p+t)//w
tq = (q+t)//h

if tp % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if tq % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)


'''
# 1. 시간 초과

# 행: h, 열: w
w, h = map(int, input().split())
# arr = [[0] * w for _ in range(h)]

p, q = map(int, input().split())
# 처음 개미 위치: x, y
c = p
r = h-q
ni = -1
nj = 1
t = int(input())

for i in range(t):
    if (r == 0 or r == h) and (c == 0 or c == w):   # 모서리
        ni *= -1
        nj *= -1
        r += ni
        c += nj

    elif r == 0 or r == h:      # 북, 남
        ni *= -1
        r += ni
        c += nj

    elif c == 0 or c == w:
        nj *= -1
        r += ni
        c += nj

    else:
        r += ni
        c += nj

print(c, h-r)
'''

'''
# 2. 메모리 초과

import sys
sys.setrecursionlimit(200000000)
# sys.stdin = open('input.txt')

def move_(r, c, ni=-1, nj=1, cnt=0):
    if cnt == t:
        return r, c

    if ( r == 0 or r == h ) and ( c == 0 or c == w ):   # 모서리
        ni *= -1
        nj *= -1
        r += ni
        c += nj
        cnt += 1
        return move_(r, c, ni, nj, cnt)

    if r == 0 or r == h:      # 북, 남
        ni *= -1
        r += ni
        c += nj
        cnt += 1
        return move_(r, c, ni, nj, cnt)

    elif c == 0 or c == w:
        nj *= -1
        r += ni
        c += nj
        cnt += 1
        return move_(r, c, ni, nj, cnt)

    r += ni
    c += nj
    cnt += 1
    return move_(r, c, ni, nj, cnt)

# 행: h, 열: w
w, h = map(int, input().split())
# arr = [[0] * w for _ in range(h)]

p, q = map(int, input().split())
# 처음 개미 위치: x, y
y = p
x = h-q

t = int(input())
ant_x, ant_y = move_(x, y)
print(ant_y, h-ant_x)
'''