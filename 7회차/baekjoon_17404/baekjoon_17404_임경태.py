# 17404 RGB 거리 2 (골드4)

N, ans = int(input()), 1000000
rgb = [list(map(int, input().split())) for _ in range(N)]

# 시작점을 바꾸어가며 순회
for i in range(3):
    rgb2 = [i[:] for i in rgb]

    # DP 시작
    for j in range(1, N):
        for k in range(3):
            # 두번째 집 칠할때 첫번째 집과 동일한 색상은 최대값을 주어 배제
            if j == 1:
                if k != i: rgb2[1][k] += rgb2[0][i]
                else: rgb2[1][k] = 2000
            else:
                # 마지막 집이 첫번째 집과 색이 같으면 최대값을 주어 배제
                if j == N-1 and k == i: rgb2[j][k] = 1000000
                else: rgb2[j][k] += min(rgb2[j-1][k-1], rgb2[j-1][k-2])

    ans = min(ans, min(rgb2[-1]))

print(ans)