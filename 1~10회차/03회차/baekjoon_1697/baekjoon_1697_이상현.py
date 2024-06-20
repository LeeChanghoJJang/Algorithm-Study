# 백준 1697번 숨바꼭질

from collections import deque

# bfs를 이용하여 접근
def bfs(n, k):
    queue = deque()

    # 큐에는 튜플 형태의 자료를 저장하는데
    # 0번째 원소는 현재 위치이고, 1번째 원소는 현재까지 소모된 시간을 나타냄
    queue.append((n, 0))
    visited = [0] * 100001

    while queue:
        current, cnt = queue.popleft()

        # 만약 동생을 찾았다면 그때까지 걸린 시간을 반환
        if current == k:
            return cnt

        for npos in [current - 1, current + 1, 2 * current]:

            # 범위를 벗어나거나 이미 방문한 곳이라면 다음으로 넘어감
            if 0 <= npos <= 100000 and not visited[npos]:
                visited[npos] = 1
                queue.append((npos, cnt + 1))

n, k = map(int, input().split())

# bfs 방식이므로 무조건 최솟값이 나옴
print(bfs(n, k))