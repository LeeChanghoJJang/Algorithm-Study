# 11437 LCA (골드3)

from collections import deque

# 트리 생성
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# 노드 높이 배열 & 부모 노드 배열 생성
dep = [0] * (N+1); dep[1] = 1
anc = [0] * (N+1); Q = deque([1])
while Q:
    s = Q.popleft()
    for e in tree[s]:
        if not dep[e]:
            dep[e] = dep[s] + 1
            anc[e] = s
            Q.append(e)

# 최소 공통 조상 검색
def LCA(c1, c2):
    if dep[c1] > dep[c2]:
        c1, c2 = c2, c1

    while dep[c1] < dep[c2]:
        c2 = anc[c2]

    while c1 != c2:
        c1 = anc[c1]
        c2 = anc[c2]
    
    return c1

# 데이터 캐싱을 통한 계산 효율 극대화 (5배) - 단일 케이스에는 효과 없음
cache = {}
for _ in range(int(input())):
    c1, c2 = map(int, input().split())

    if (c1, c2) not in cache:
        cache[(c1, c2)] = cache[(c2, c1)] = LCA(c1, c2)

    print(cache[(c1, c2)])

'''
43228KB / 244ms
'''


# 메모리 초과
'''
def find_p(n):
    p, parents = n, []
    while p:
        parents.append(p)
        p = tree[p]
    return parents

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N-1)]
tree = [0] * (N+1)

while 0 in tree[2:]:
    for s, e in info:
        if tree[s] and tree[e]: pass
        elif tree[s] or s == 1: tree[e] = s
        elif tree[e] or e == 1: tree[s] = e

for i in range(int(input())):
    n1, n2 = map(int, input().split())
    for j in find_p(n1):
        if j in find_p(n2): print(j); break
'''