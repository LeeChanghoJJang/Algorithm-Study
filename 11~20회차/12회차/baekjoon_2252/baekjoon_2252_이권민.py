import sys

# 재귀 호출의 깊이 한계를 늘림
sys.setrecursionlimit(10 ** 8)

def Recur(a):
    if not Nodes[a][0] and visited[a] == 0:
        result.append(a)
        visited[a] = 1
    # 부모가 없고 안가봄
    elif Nodes[a][0] and visited[a] == 0:
        for i in Nodes[a][0]:
            if visited[i] == 0:
                
                Recur(i)
        visited[a] = 1
        result.append(a)
    # 부모가 있고 안가봄 -> 부모로
        
N,M = map(int,input().split())
Nodes = [[[],[]] for _ in range(N+1)]
# 앞에가 부모, 뒤에가 자식
for _ in range(M):
    par,chl = map(int,input().split())
    Nodes[par][1].append(chl)
    Nodes[chl][0].append(par)
visited = [0]*(N+1)
result = []

for i in range(1,N+1):
    Recur(i)
        
print(*result)

    
        
    