import sys
sys.stdin = open('input.txt')

ds = ((-1, 0), (1, 0), (0, -1), (0, 1))

for tc in range(int(input())):
    N, M = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0

    for x in range(N):
        for y in range(M):
            count = data[x][y]
            for dx, dy in ds:
                nx, ny = x + dx, y + dy
                if 0<=nx<N and 0<=ny<M:
                    count += data[nx][ny]
            ans = max(ans, count)

    print(f'#{tc+1} {ans}')
