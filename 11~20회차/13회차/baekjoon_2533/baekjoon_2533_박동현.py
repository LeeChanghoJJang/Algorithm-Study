import sys
sys.setrecursionlimit(10**6)


input = sys.stdin.readline


N = int(input())

graph = [ [] for _ in range(N+1) ]


for _ in range(N-1) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visit = [False] * (N+1)

# DP[i][j]
# i : 정점 번호
# j : 0/1 자신이 얼리어답터인지 아닌지 체크
DP = [ [0,0] for _ in range(N+1) ]

def DFS(now=1):
    visit[now] = True
    DP[now][0] = 0
    DP[now][1] = 1

    for next in graph[now] :
        if not visit[next] :
            DFS(next)
            DP[now][0] += DP[next][1]       # 내가 얼리어답터가 아니면 자식이 얼리어답터여야함
            DP[now][1] += min(DP[next])     # 내가 얼리어답터면 알빠노


DFS()
print(min(DP[1]))