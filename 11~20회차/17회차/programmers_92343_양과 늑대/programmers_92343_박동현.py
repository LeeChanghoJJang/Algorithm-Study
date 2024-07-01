def solution(info, edges):
    answer = 0
    tree = [[] for _ in range(len(info))]
    for s,e in edges:
        tree[s].append(e)

    def DFS(now=0, sheep=0, wolf=0, stack=[0]):
        nonlocal answer  # global 대용
        # 양 늑대 마리수 계산
        if info[now] == 1:
            wolf += 1
        else:
            sheep += 1
        # 양이 늑대보다 적으면 끝
        if wolf >= sheep:
            return
        # answer 계산
        answer = max(answer, sheep)
        # DFS 하러 내려감
        for next_node in stack:
            for next in tree[next_node]:
                if next not in stack:
                    DFS(next, sheep, wolf, stack + [next])

    DFS()
    
    return answer