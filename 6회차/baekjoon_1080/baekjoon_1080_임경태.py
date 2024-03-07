# 1080 행렬

N, M, cnt = map(int, input().split()), 0
A, B = [input() for _ in range(N)], [input() for _ in range(N)]
# 두 행렬값의 차 행렬을 만들어 모두 0 인지 체크
sub = [[abs(int(a) - int(b)) for a, b in zip(A[i], B[i])] for i in range(N)]

for i in range(N):
    for j in range(M):
        if sub[i][j]:  # 차이가 있고
            if i < N - 2 and j < M - 2:  # 뒤 부분에 충분히 바꿀만한 공간이 있으면 바꿈
                for ci in range(3):
                    for cj in range(3):
                        sub[i+ci][j+cj] = 1 - sub[i+ci][j+cj]
                cnt += 1
            else:  # 뒤 부분에 바꿀 공간이 없으면 불가능
                exit(print(-1))
print(cnt)

'''
31120KB / 48ms
'''