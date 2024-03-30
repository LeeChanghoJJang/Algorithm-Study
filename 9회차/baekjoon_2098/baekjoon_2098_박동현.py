import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dp = {}

now = 0 
visit = 1

def DFS(now=0, visit=1) :
    if visit == (1 << N) -1 :
        if arr[now][0]:
            return arr[now][0]
        else :
            return int(1e9)
    
    if (now,visit) in dp:
        return dp[(now, visit)]
    
    min_cost = int(1e9)
    for next in range(1,N):
        if arr[now][next] == 0 or visit & ( 1<< next) :
            continue
        cost = DFS(next,visit | (1<<next)) + arr[now][next]
        min_cost = min(min_cost, cost)

    dp[(now,visit)] = min_cost
    return min_cost

print(DFS())