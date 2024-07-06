from collections import deque,defaultdict

def solution(info,edges):
    graph = defaultdict(list)

    for parent,child in edges:
        graph[parent].append(child)

    max_sheep = 0

    def dfs(sheep,wolf,current,path):
        nonlocal max_sheep
        max_sheep = max(max_sheep,sheep)

        for node in path:
            for next_node in graph[node]:
                if next_node not in path:
                    if info[next_node]==0:
                        dfs(sheep+1,wolf,current,path|{next_node})
                    else:
                        if sheep > wolf + 1:
                            dfs(sheep,wolf+1,current,path|{next_node})

    dfs(1,0,0,{0})

    return max_sheep