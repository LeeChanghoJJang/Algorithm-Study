import sys
sys.setrecursionlimit(10**5)

def dfs(x=1,depth=0):               # dfs 를 통한 부모 노드 탐색 (루트=1)

    visited[x] = 1                  # 방문 표시
    
    d[x] = depth                    # d 의 인덱스에 노드의 깊이를 저장

    for i in graph[x]:
        if not visited[i]:
            parent[i]=x             # 부모 저장
            dfs(i,depth+1)

def lca(a,b):

    while d[a] != d[b]:             # 노드의 깊이가 안맞는 경우
        if d[a] > d[b]:
            a = parent[a]           # 한칸씩 올림
        else:
            b= parent[b]

    while a!=b:                     # 깊이 맞춘 뒤에는 하나씩 올라가면서 조상 탐색
        a = parent[a]
        b = parent[b]

    return a                        # 반환


N = int(input())

graph = [[] for _ in range(N+1)]    # 인접 그래프 

for i in range(N-1):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

parent = [i for i in range(N+1)]    # 부모 인덱스 저장 리스트 

visited = [0] * (N+1)               # 방문 확인 리스트

d = [0]*(N+1)                       # 깊이 저장 리스트

dfs()

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))                # 출력