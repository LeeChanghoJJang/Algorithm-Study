n = int(input())
temp = []
visited = [[False] * n for _ in range(n)]

def dfs(x, y, visited):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if not visited[x][y] and temp[x][y] != 0:
        visited[x][y] = True
        temp[x][y] += result
        
        dfs(x-1, y, visited)
        dfs(x, y-1, visited)
        dfs(x+1, y, visited)
        dfs(x, y+1, visited)
        return True
    
    return False

for i in range(n):
    temp.append(list(map(int, input())))
    
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j, visited) == True:
            result += 1
            
print(result)

buildings = []

for i in range(1, result+1):
    count = 0
    
    for j in range(n):
        for k in range(n):
            if temp[j][k] == i:
                count += 1
                
    buildings.append(count)
    buildings.sort()
    
for _ in buildings:
    print(_)