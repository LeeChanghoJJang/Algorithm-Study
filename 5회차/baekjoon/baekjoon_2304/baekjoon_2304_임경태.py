# 2304 창고 다각형

import sys
sys.stdin = open('input.txt')

def cal(start, end, rev):
    global area
    local_high = 0
    for i in range(start, end, rev):
        if i in idx:
            local_high = max(local_high, h[idx.index(i)])
        area += local_high

N = int(input())
idx, h = list(zip(*sorted(list(map(int, input().split())) for _ in range(N))))
h_idx = idx[h.index(max(h))]
area = max(h)

cal(idx[0], h_idx, 1)
cal(idx[-1], h_idx, -1)

print(area)

'''
31120KB / 52ms
'''