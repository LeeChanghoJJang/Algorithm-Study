# 2606 바이러스

'''
풀이 1 : BFS    34016KB / 64ms
'''
from collections import deque

Q = deque([1])                    # 덱
V = int(input())                  # 컴퓨터 개수
E = int(input())                  # 연결쌍 개수
NW = [[] for _ in range(V + 1)]   # 연결 번호 목록
visited = [None] * (V + 1)        # 방문 확인

# 연결 번호 목록 입력
for _ in range(E):
    n1, n2 = map(int, input().split())
    NW[n1].append(n2)
    NW[n2].append(n1)

# BFS 실행
cnt = 0
while Q:
    n1 = Q.popleft()
    for n2 in NW[n1]:
        if not visited[n2] and n2 != 1:
            visited[n2] = 1
            cnt += 1
            Q.append(n2)

print(cnt)

'''
풀이 2 : DFS    31120KB / 40ms
'''
V = int(input())                  # 컴퓨터 개수
E = int(input())                  # 연결쌍 개수
NW = [[] for _ in range(V + 1)]   # 연결 번호 목록
visited = [False] * (V + 1)       # 방문 확인

# 연결 번호 목록 입력
for _ in range(E):
    n1, n2 = map(int, input().split())
    NW[n1].append(n2)
    NW[n2].append(n1)

# DFS 실행
def DFS(n1):
    global cnt
    for n2 in NW[n1]:
        if not visited[n2] and n2 != 1:
            visited[n2] = True
            cnt += 1
            DFS(n2)

cnt = 0
DFS(1)
print(cnt)