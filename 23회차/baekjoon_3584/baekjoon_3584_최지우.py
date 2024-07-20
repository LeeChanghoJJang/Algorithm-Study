def dfs(v):
    stack = [v]
    i = 0
    while stack:
        cur = stack.pop()
        par = tree[cur]
        if par:
            if not visited[par]:
                stack.append(par)
                visited[par] = 1
            else:
                return print(par)
    

T = int(input())
for _ in range(T):
    N = int(input())
    tree = [0] * (N+1)
    
    for _ in range(N-1):
        A, B = map(int, input().split())
        tree[B] = A
    x, y = map(int, input().split())
    visited = [0] * (N+1)
    visited[x] = 1
    visited[y] = 1
    dfs(x)
    dfs(y)
    