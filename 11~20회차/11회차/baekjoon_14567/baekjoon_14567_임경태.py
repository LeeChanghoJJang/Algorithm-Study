# 14567 선수과목 (Prerequisite)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
depth = [1] * (N+1)

# 그래프 생성
for _ in range(M):
    pre, post = map(int, input().split())
    graph[pre].append(post)

# 진입 차수 계산
for now in range(1, N+1):
    for next in graph[now]:
        depth[next] = max(depth[next], depth[now] + 1)

print(*depth[1:])

'''
    <위상 정렬(topological sorting)>
    유향 그래프의 노드들을 간선의 방향을 거스르지 않도록 나열하는 것
    선후 관계가 정의된 그래프 구조 상에서 선후 관계에 따라 정렬하기 위해 위상 정렬을 이용할 수 있다.
    위상 정렬이 성립하기 위해서는 반드시 그래프의 순환이 존재하지 않아야 한다.
    주로 선수 과목을 정하는 문제나 작업 스케줄링 문제에 사용

    수행과정
    1. 자기 자신을 가리키는 간선이 없는 노드를 찾음
    2. 찾은 노드를 출력하고 출력한 노드와 그 노드에서 출발하는 간선을 삭제
    3. 아직 그래프에 노드가 남아있으면 단계 1로 돌아가고, 아니면 알고리즘을 종료
'''