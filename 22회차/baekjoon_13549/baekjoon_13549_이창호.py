from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.read
n, k = map(int, input().split())

def bfs(n, k):
    if n >= k:
        return n - k

    maximum = 100001
    dp = [float('inf')] * maximum
    visited = [False] * maximum
    queue = deque([n])
    dp[n] = 0
    visited[n] = True

    while queue:
        current = queue.popleft()
        if current == k:
            return dp[current]

        for next in [current - 1, current + 1, current * 2]:
            if 0 <= next < maximum and not visited[next]:
                visited[next] = True
                if next == current * 2:
                    dp[next] = dp[current]
                    queue.appendleft(next)  # 순간이동은 0초이므로 우선적으로 처리
                else:
                    dp[next] = dp[current] + 1
                    queue.append(next)

    return -1

print(bfs(n, k))
