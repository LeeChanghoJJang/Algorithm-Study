# 백준 1865번 웜홀

# 벨만 포드 알고리즘
def bf():
    for i in range(N):
        for j in range(len(edges)):
            current_v, next_v, cost = edges[j]

            if dist[next_v] > dist[current_v] + cost:
                dist[next_v] = dist[current_v] + cost

                if i == N - 1:
                    return True
    return False

T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []
    dist = [10e9] * (N + 1)

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    print('YES' if bf() else 'NO')