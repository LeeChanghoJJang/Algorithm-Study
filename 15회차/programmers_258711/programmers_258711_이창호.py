def solution(edges):
    answer = [0, 0, 0, 0]  # 생성 정점, 도넛, 막대, 8자
    max_val = max(map(max, edges)) + 1  # +1 은 인덱스 맞춰주기 위함
    in_degree, out_degree = [0] * max_val, [0] * max_val

    # in, out 간선 저장
    for now_out, now_in in edges:
        out_degree[now_out] += 1
        in_degree[now_in] += 1

    for now_node in range(1, max_val):
        # 생성정점은 최상위 노드같이 맨 처음에 시작
        if in_degree[now_node] == 0 and out_degree[now_node] >= 2:  # 생성 노드
            answer[0] = now_node
        # 막대그래프는 들어오는게 1개 이상이고 나가는 것이 없을 때
        elif in_degree[now_node] >= 1 and out_degree[now_node] == 0:  # 막대 그래프
            answer[2] += 1
        # 들어오는 것이 2개 이상이고, 나가는것도 2개 이상
        elif in_degree[now_node] >= 2 and out_degree[now_node] == 2:  # 8자 그래프
            answer[3] += 1
    # 도넛은 생성정점의 아웃 개수 - 위 두개 그래프 갯수 빼면 됨
    answer[1] = out_degree[answer[0]] - sum(answer[2:])  # 도넛 그래프

    return answer