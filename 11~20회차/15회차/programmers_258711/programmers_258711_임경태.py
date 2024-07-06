# 도넛과 막대 그래프 (2024 KAKAO WINTER INTERNSHIP)

def solution(edges):  
    answer = [0, 0, 0, 0]  # 생성한 정점 번호, 도넛 모양 그래프 수, 막대 모양 그래프 수, 8자 모양 그래프 수
    edge_counts = {}  # 각 노드별 간선의 수

    for a, b in edges:
        # [나가는 간선 개수, 들어오는 간선 개수]
        if not edge_counts.get(a): edge_counts[a] = [0, 0]
        if not edge_counts.get(b): edge_counts[b] = [0, 0]

        # 나가는 간선과 들어오는 간선 개수 추가
        edge_counts[a][0] += 1
        edge_counts[b][1] += 1

    for edge, counts in edge_counts.items():
        # 생성한 정점의 번호
        if counts[0] >= 2 and counts[1] == 0: answer[0] = edge

        # 막대 모양 그래프의 수 계산
        elif counts[0] == 0 and counts[1] > 0: answer[2] += 1

        # 8자 모양 그래프의 수 계산
        elif counts[0] >= 2 and counts[1] >= 2: answer[3] += 1

    # 도넛 모양 그래프의 수 계산
    answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3])

    return answer