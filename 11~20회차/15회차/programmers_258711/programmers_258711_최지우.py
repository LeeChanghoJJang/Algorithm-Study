# 도넛과 막대그래프 lv2
def solution(edges):
    edge = set()
    e_out = {}
    e_in = {}
    for s, e in edges:
        e_out[s] = e_out.setdefault(s, 0) + 1
        e_in[e] = e_in.setdefault(e, 0) + 1
        edge.add(s)
        edge.add(e)

    new_node = donut = rod = eight = 0
    graph_cnt = 0

    for i in edge:
        if i in e_out:
            if e_out[i] >= 2:
                if i not in e_in:
                    new_node = i
                    graph_cnt = e_out[new_node]
                else:
                    eight += 1
        else:
            if i in e_in:
                rod += 1

    donut = graph_cnt - rod - eight
    answer = [new_node, donut, rod, eight]
    return answer


'''
    input: [방향 있는 간선 edges]
    output: [생성한 정점 번호, 도넛, 막대, 8자 그래프 수]
    
    나가는 점만 가진 정점: 생성한 노드
    나가는 점 2 들어오는 점 2 정점 =>  8자
    
    들어오는 점 1 => 마지막에 원점으로 오면 도넛 / 나가는 점 없어지면 막대
    
    각 노드별,
    경우 1) out==0: ---> 직선 그래프 갯수 +=1
    경우 2) out==1: 흔한 노드.. 무시
    경우 3) out==2:
            if in>0: ---> 8자 그래프 갯수 +=1
            else: ---> 이 노드가 시작 정점
    경우 4) out>2: ---> 이 노드가 시작 정점

'''

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
# edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

print(solution(edges))