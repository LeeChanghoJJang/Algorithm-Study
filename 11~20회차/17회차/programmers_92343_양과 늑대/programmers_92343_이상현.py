def solution(info, edges):
    answer = 0
    visited = [False] * len(info)
    
    visited[0] = True
    answer = dfs(1, 0, info, edges, visited)
    
    return answer

def dfs(sheep, wolf, info, edges, visited):
    if sheep <= wolf:
        return sheep - 1
    
    max_sheep = sheep
    
    for prev, cur in edges:
        if visited[prev] and not visited[cur]:
            visited[cur] = True
            
            if info[cur]:
                max_sheep = max(max_sheep, dfs(sheep, wolf + 1, info, edges, visited))
            else:
                max_sheep = max(max_sheep, dfs(sheep + 1, wolf, info, edges, visited))
                
            visited[cur] = False
            
    return max_sheep