s_list = [[0, 0] for _ in range(7)]
N, K = map(int, input().split())

for _ in range(N):
    S, Y = map(int, input().split())
    s_list[Y][S] += 1

cnt = 0

for y in range(1, 7):
    if s_list[y][0]:
        cnt += 1 + (s_list[y][0] - 1) // K

    if s_list[y][1]:
        cnt += 1 + (s_list[y][1] - 1) // K

print(cnt)