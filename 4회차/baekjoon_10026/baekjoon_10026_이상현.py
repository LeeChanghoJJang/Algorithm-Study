import sys
sys.setrecursionlimit(10**6)

# 백준 10026번 적록색약

# 적록색약인 사람이 봤을 때의 구역의 수와
# 적록색약이 아닌 사람이 봤을 때의 구역의 수를 구하는 문제

# 유기농 배추와 비슷하게 품
n = int(input())
temp = [list(input()) for i in range(n)]
visited = [[False] * n for i in range(n)]

def dfs(x, y, ch, visited):
    # 범위를 벗어나면 함수 종료
    if not (0 <= x < n and 0 <= y < n):
        return False
    
    # 만약 현재 구역이 탐색중인 색 ch이고 방문하지 않았다면,
    # 방문 처리 후 주변 구역을 탐색하기 위해 함수 재귀 호출
    if temp[x][y] == ch and visited[x][y] == False:
        visited[x][y] = True
        dfs(x-1, y, ch, visited)
        dfs(x, y-1, ch, visited)
        dfs(x+1, y, ch, visited)
        dfs(x, y+1, ch, visited)

        # 같은 색으로 연결된 구역을 모두 탐색했다면
        # True를 반환
        return True
    return False

arr = ['R', 'G', 'B']
count = 0

for i in arr:
    for j in range(n):
        for k in range(n):
            # 각 색마다 구역을 탐색 후 구별되는 구역의 수를 구하는 과정
            if dfs(j, k, i, visited):
                count += 1
                
print(count)

# 위는 적록색약이 아닌 사람의 경우이고,
# 아래는 적록색약인 사람의 경우를 고려

# 과정은 적록색약이 아닌 사람의 경우와 유사하게 구함
count = 0
visited = [[False] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if temp[i][j] == 'G':
            temp[i][j] = 'R'
            
arr = ['R', 'B']
for i in arr:
    for j in range(n):
        for k in range(n):
            if dfs(j, k, i, visited):
                count += 1
                
print(count)