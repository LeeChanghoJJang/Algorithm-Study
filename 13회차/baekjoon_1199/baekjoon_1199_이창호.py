import sys
from collections import defaultdict

# 입력 파일을 열어서 stdin으로 설정합니다.
sys.stdin = open('input.txt')

# 정점의 개수를 입력으로 받습니다.
n = int(input())

# 입력을 더 빠르게 받기 위해 sys.stdin.readline()을 사용합니다.
input = sys.stdin.readline

# 그래프를 저장할 리스트와 각 정점의 차수를 저장할 리스트를 초기화합니다.
graph = []
degree = [0] * n

# 방문한 간선을 체크하기 위한 2차원 리스트를 초기화합니다.
visit = [[0] * n for _ in range(n)]

# 그래프를 입력받습니다.
for i in range(n):
    lst = {}
    for j, v in enumerate(list(map(int, input().split()))):
        if v:
            lst[j] = 1
            visit[i][j] = v
            degree[i] += v
    graph.append(lst)

# 각 정점의 차수가 홀수인지 확인합니다.
for i in range(n):
    if degree[i] % 2:
        print(-1)  # 만약 홀수인 경우 오일러 회로/경로가 존재하지 않음을 알립니다.
        sys.exit() # 프로그램을 종료합니다.

# 오일러 회로/경로를 구성할 정점을 저장할 리스트를 초기화합니다.
answer = []

# 스택을 이용한 DFS를 수행합니다.
stack = [0]
while stack:
    current = stack[-1]
    if graph[current]:
        _next = next(iter(graph[current]))
        visit[_next][current] -= 1
        visit[current][_next] -= 1
        degree[current] -= 1
        degree[_next] -= 1

        if not visit[current][_next]:
            del graph[current][_next]
            del graph[_next][current]
        stack.append(_next)
    else:
        answer.append(stack.pop() + 1)

# 모든 간선을 방문했는지 확인합니다.
for i in range(n):
    if degree[i]:
        print(-1)  # 모든 간선을 방문하지 않은 경우 오일러 회로/경로가 존재하지 않음을 알립니다.
        sys.exit() # 프로그램을 종료합니다.

# 결과를 출력합니다.
print(' '.join(map(str,answer)))
