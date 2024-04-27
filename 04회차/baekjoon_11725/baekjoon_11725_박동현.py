import sys
# from collections import deque

t = int(input())

tree = [[] for _ in range(t+1)]
for _ in range(t-1):
    V,W = map(int,sys.stdin.readline().strip().split())
    tree[V].append(W)       # 트리의 루트가 없으므로 일단 둘다 저장
    tree[W].append(V)

q = [1]              # 1을 정점으로 하여 parent를 설정해 내려가면서 탐색
parent = [0] * (t+1)

while q:
    tc = q.pop()

    for item in tree[tc]:       # 트리에 간선이 있는 경우
        if parent[item] == 0:   # 그곳을 들리지 않았으면
            parent[item] = tc   # 이러면 item의 부모는 tc 
            q.append(item)      # 계속 탐색

print(*parent[2:], sep="\n")    

# 덱 사용 BFS 52104kb / 304ms
# 리스트 사용 DFS 51412kb / 272ms