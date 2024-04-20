dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(v, cnt):
    global result
    x, y = v

    if result == 26:
        return

    result = max(cnt, result)
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            char = ord(arr[nx][ny]) - 64
            if not used[char]:
                used[char] = 1
                bfs((nx, ny), cnt + 1)
                used[char] = 0


R, C = map(int, input().split())
arr = [list(map(str, input())) for _ in range(R)]

used = [0] * 27
start = ord(arr[0][0]) - 64
used[start] = 1

result = 0
bfs((0, 0), 1)

print(result)
