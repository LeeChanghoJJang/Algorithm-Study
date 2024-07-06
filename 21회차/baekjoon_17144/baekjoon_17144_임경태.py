# 17144 미세먼지 안녕!

def diffusion(room):
    new_room = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if room[i][j] == -1 or not room[i][j]: continue

            df_dust = room[i][j] // 5
            
            for dj, di in dir_U:
                ni, nj = i + dj, j + di
                
                if 0<=ni<R and 0<=nj<C and room[ni][nj] != -1:
                    new_room[ni][nj] += df_dust
                    room[i][j] -= df_dust

            new_room[i][j] += room[i][j]

    return new_room

def cleaner(dr, pos):
    i, j = pos, 1
    dir = bef = 0

    while True:
        ni, nj = i + dr[dir][0], j + dr[dir][1]

        # 순환 완료
        if (i, j) == (pos, 0):
            room[i][j] = 0
            break

        # 방향 전환
        if not (0<=ni<R and 0<=nj<C):
            dir += 1
            continue

        room[i][j], bef = bef, room[i][j]
        i, j = ni, nj


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
air = [i for i in range(R) if room[i][0] == -1]
dir_U = (0, 1), (-1, 0), (0, -1), (1, 0)
dir_D = (0, 1), (1, 0), (0, -1), (-1, 0)

# 공기청정기 가동
for _ in range(T):
    room = diffusion(room)
    cleaner(dir_U, air[0])
    cleaner(dir_D, air[1])

print(sum(sum(row) for row in room))
