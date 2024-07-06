from collections import deque

def is_connected(left, right):
    global min_, total_p

    left_set = set(left)
    right_set = set(right)

    q = deque([left[0]])
    visited = [False] * (N + 1)
    visited[left[0]] = True
    sum_ = 0

    while q:
        vertex = q.popleft()
        sum_ += p_list[vertex]

        for v in graph[vertex]:
            if v in right_set or visited[v]:
                continue
            visited[v] = True
            q.append(v)

    if any(not visited[v] for v in left):
        return

    q = deque([right[0]])
    visited[right[0]] = True

    while q:
        vertex = q.popleft()

        for v in graph[vertex]:
            if v in left_set or visited[v]:
                continue
            visited[v] = True
            q.append(v)

    if any(not visited[v] for v in right):
        return

    min_ = min(min_, abs(total_p - 2 * sum_))

N = int(input())
p_list = [0] + list(map(int, input().split()))
total_p = sum(p_list)
graph = [[] for _ in range(N + 1)]
min_ = 1000

for v in range(1, N + 1):
    _, *temp = map(int, input().split())

    for nbd in temp:
        graph[v].append(nbd)

for i in range(1 << N):
    left = []
    cnt = 0

    for j in range(N):
        if i & (1 << j):
            left.append(j + 1)
            cnt += 1

    if cnt == 0 or cnt == N:
        continue

    right = [v for v in range(1, N + 1) if v not in left]
    is_connected(left, right)

print(min_ if min_ != 1000 else -1)