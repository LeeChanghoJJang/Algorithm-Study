from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = {start}
    target = ''.join(sorted(start))

    while q:
        current, cnt = q.popleft()

        if current == target:
            return cnt

        for i in range(N - K + 1):
            temp = current[:i] + ''.join(reversed(list(current[i:i + K]))) + current[i + K:]

            if temp in visited:
                continue

            visited.add(temp)
            q.append((temp, cnt + 1))

    return -1

N, K = map(int, input().split())
list_ = input().split()
print(bfs(''.join(list_)))