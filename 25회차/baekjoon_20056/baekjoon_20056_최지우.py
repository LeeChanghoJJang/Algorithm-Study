import sys
input = sys.stdin.readline
from collections import defaultdict

def move_fb(N, fb):
    new_fb_dict = defaultdict(list)
    for r, c, m, s, d in fb:
        nr, nc = r + dr[d][0] * s, c + dr[d][1] * s
        nr, nc = nr%N, nc%N
        new_fb_dict[(nr, nc)].append((m, s, d))
    return new_fb_dict


def new_fb(N, fb_dict):
    new_fb = []
    for (r, c), fbs in fb_dict.items():
        if len(fbs) > 1:
            total_m, total_s, cnt = 0, 0, len(fbs)
            dr_set = set()
            for m, s, d in fbs:
                total_m += m
                total_s += s
                dr_set.add(d%2)
            
            if total_m // 5 > 0:
                new_m = total_m // 5
                new_s = total_s // cnt
                if len(dr_set) == 1:
                    new_dr = [0, 2, 4, 6]
                else:
                    new_dr = [1, 3, 5, 7]
                
                for d in new_dr:
                    new_fb.append((r, c, new_m, new_s, d))
        else:
            new_fb.append((r, c) + fbs[0])

    return new_fb

N, M, K = map(int, input().split())

dr = [(-1, 0), (-1, 1), (0, 1), (1, 1),
      (1, 0), (1, -1), (0, -1), (-1, -1)]

fb = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    fb.append((r, c, m, s, d))

for _ in range(K):
    fb_dict = move_fb(N, fb)
    fb = new_fb(N, fb_dict)

result = sum(m for r, c, m, s, d in fb)
print(result)
