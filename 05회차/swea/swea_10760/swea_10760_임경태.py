import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0, -1, -1,  1,  1]
dy = [0, 0, -1, 1, -1,  1, -1,  1]

def search(x, y):
    point = data[x][y]
    count = 0

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if point > data[nx][ny]:
                count += 1
                if count >= 4:
                    return True
    return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for x in range(N):
        for y in range(M):
            result += search(x, y)

    print(f'#{tc} {result}')
