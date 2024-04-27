# 15663 N과 M (9)

# 방법1 - DFS : 35732KB / 132ms
def per(i, arr):
    if len(arr) == M:
        global ans; ans.add(tuple(arr))
        return
    for j in range(i, N):
        num[i], num[j] = num[j], num[i]
        per(i+1, arr + [num[i]])
        num[i], num[j] = num[j], num[i]

N, M = map(int, input().split())
num = list(map(int, input().split()))
ans = set()
per(0, [])
for p in sorted(ans): print(*p)

# 방법2 - 라이브러리 : 35732KB / 112ms
from itertools import permutations
N, M = map(int, input().split())
perms = sorted(set(permutations(map(int, input().split()), M)))
for p in perms: print(*p)
