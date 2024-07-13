from collections import deque

def bfs(n, k):
    queue = deque()
    queue.append((n, 0))
    visited = [0] * 100001

    while queue:
        current, cnt = queue.popleft()

        if current == k:
            return cnt

        temp = 2 * current

        if 0 <= temp <= 100000 and not visited[temp]:
            visited[temp] = 1
            queue.append((temp, cnt))

        for npos in [current - 1, current + 1]:
            if 0 <= npos <= 100000 and not visited[npos]:
                visited[npos] = 1
                queue.append((npos, cnt + 1))

n, k = map(int, input().split())
print(bfs(n, k))