from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n+1)
temp = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    temp[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        c = q.popleft()
        result.append(c)
        
        for j in temp[c]:
            indegree[j] -= 1
            
            if indegree[j] == 0:
                q.append(j)
                
    for k in result:
        print(k, end = ' ')
        
topology_sort()