# 루트노드, 도넛, 막대, 8자
def solution(edges):
    answer = [0, 0, 0, 0]
    max_node = max(map(max, edges)) + 1   # 제일 큰 노드
    in_cnt, out_cnt = [0] * max_node, [0] * max_node

    # 각 노드에 나가는 숫자랑 들어오는 숫자 확인
    for s, e in edges:
        in_cnt[e] += 1
        out_cnt[s] += 1
    for n in range(1, max_node):
        if in_cnt[n] == 0 and out_cnt[n] >= 2:  # 루트 노드
            answer[0] = n
        elif in_cnt[n] >= 1 and out_cnt[n] == 0:    # 막대
            answer[2] += 1
        elif in_cnt[n] >= 2 and out_cnt[n] == 2:    # 8자
            answer[3] += 1
    answer[1] = out_cnt[answer[0]] - sum(answer[2:])    # 도넛
    return answer

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))