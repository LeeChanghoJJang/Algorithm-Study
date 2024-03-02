import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
n = int(input())
block = [0] * (2*(w+h))

# 각 객체 마킹
for i in range(1, n+2):
    d, l = map(int, input().split())
    if d == 3: block[h-l] = i
    elif d == 1: block[h+l] = i
    elif d == 4: block[h+w+l] = i
    else: block[-l] = i

dist = 0
cur = block.index(n+1)  # 경비원 위치

# 각 지점별 최소 거리 합산
for i in range(1, n+1):
    alm = block.index(i)
    dist += min(abs(cur-alm), abs(len(block)-cur+alm))

print(dist)

'''
31120KB / 40ms
'''