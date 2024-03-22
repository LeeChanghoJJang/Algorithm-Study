import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 들어온 방향, 나온 방향 블럭 별로 저장
block = [
    [],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]

def pinball(x, y, d):
    check = 0

    ni = x
    nj = y
    while 1:        # 게임 끝날때 까지
        ni += di[d]
        nj += dj[d]

        if (ni, nj) == (x, y) or arr[ni][nj] == -1:     # 게임 끝나는 조건
            return check

        if 1 <= arr[ni][nj] <= 5:       # block
            d = block[arr[ni][nj]][d]
            check += 1
        elif arr[ni][nj] == 0:
            pass
        else:   # 웜홀
            ni, nj = wormhole[(ni, nj)]


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n = int(input())
    wormhole = {}
    wormhole_visited = [0] * 11

    # arr 만들기
    arr = [[5] * (n+2)]
    for i in range(1, n+1):
        arr.append([5] + list(map(int, input().split())) + [5])
        # 웜홀
        for j in range(1, n+1):
            if 6 <= arr[i][j] <= 10:
                if not wormhole_visited[arr[i][j]]:     # 웜홀 쌍이 없으면
                    wormhole_visited[arr[i][j]] = (i, j)
                else:       # 있으면 딕셔너리에 쌍 넣기
                    wormhole[wormhole_visited[arr[i][j]]] = (i, j)
                    wormhole[(i, j)] = wormhole_visited[arr[i][j]]
    arr.append([5] * (n+2))

    # print(wormhole)
    score = float('-inf')
    # 순회하면서 최적의 출발지 찾기
    for r in range(1, n+1):
        for c in range(1, n+1):
            if arr[r][c] == 0:
                # 4 방향 다 체크해보기
                for d in range(4):
                    score = max(score, pinball(r, c, d))
    print(score)

