N = int(input())
scv = [0, 0, 0]
l = list(map(int, input().split()))


def mut(x, y, z, cnt):
    global result

    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z

    if x == 0 and y == 0 and z == 0:
        if result > cnt:
            result = cnt
            return

    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return

    dp[x][y][z] = cnt

    mut(x - 9, y - 3, z - 1, cnt + 1)
    mut(x - 9, y - 1, z - 3, cnt + 1)
    mut(x - 3, y - 9, z - 1, cnt + 1)
    mut(x - 3, y - 1, z - 9, cnt + 1)
    mut(x - 1, y - 9, z - 3, cnt + 1)
    mut(x - 1, y - 3, z - 9, cnt + 1)


for i in range(N):
    scv[i] = l[i]

result = 1e9
dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]
mut(scv[0], scv[1], scv[2], 0)
print(result)
