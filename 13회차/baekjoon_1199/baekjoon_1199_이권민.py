import sys

# 재귀 제한을 늘림
sys.setrecursionlimit(10**9)

# 정수 N 입력
N = int(sys.stdin.readline())

# 입력을 담을 2차원 리스트 생성
myList = []

# N번 반복하여 입력을 리스트에 추가
for i in range(N):
    myList.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 그래프를 나타낼 딕셔너리 생성
graph = {}

# 그래프 생성
for i in range(N):
    graph[i] = []  # 각 노드에 빈 리스트 할당
    rowSum = 0  # 현재 행의 합 초기화
    for j in range(N):
        for k in range(myList[i][j]):
            rowSum += 1  # 현재 행의 합 증가
            graph[i].append(j)  # 현재 노드와 연결된 노드를 그래프에 추가
    # 행의 합이 홀수인 경우 오일러 경로가 존재하지 않음
    # ?
    if rowSum % 2 == 1:
        print(-1)
        sys.exit()

# 깊이 우선 탐색 함수 정의
def dfs(nowNode):
    # 현재 노드에서 연결된 모든 노드에 대해 탐색
    for i in graph[nowNode]:
        # 간선이 남아있는 경우
        if myList[nowNode][i]:
            # 해당 간선 제거
            myList[nowNode][i] -= 1
            myList[i][nowNode] -= 1
            # 다음 노드로 이동하여 탐색
            dfs(i)
    # 현재 노드 출력
    print(nowNode + 1, end=" ")

# 시작 노드를 0으로 설정하여 탐색 시작
dfs(0)
