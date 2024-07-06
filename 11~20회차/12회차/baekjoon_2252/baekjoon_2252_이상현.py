from collections import deque

# 노드의 개수 n과 간선의 개수 m 입력
n, m = map(int, input().split())
# 진입차수를 저장할 리스트 초기화
indegree = [0] * (n + 1)
# 각 노드별 진입하는 노드들을 저장할 리스트 초기화
temp = [[] for _ in range(n + 1)]

# 간선 정보 입력받아 인접 리스트 구성
for i in range(m):
    a, b = map(int, input().split())
    temp[a].append(b)  # a에서 b로 이동하는 간선 추가
    indegree[b] += 1  # b의 진입차수 증가

# 위상 정렬 함수 구현
def topology_sort():
    result = []  # 위상 정렬 결과를 담을 리스트
    q = deque()  # 큐 생성

    # 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        c = q.popleft()  # 큐에서 노드 추출하여 결과 리스트에 추가
        result.append(c)

        # 해당 노드와 연결된 노드들의 진입차수를 감소시키고, 진입차수가 0이 되면 큐에 추가
        for j in temp[c]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)

    # 결과 리스트 출력
    for k in result:
        print(k, end=' ')

# 위상 정렬 함수 호출
topology_sort()
