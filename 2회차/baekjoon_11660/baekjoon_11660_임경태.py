# 11660 구간 합 구하기 5
# 구간의 합을 미리 구해놓자 - DP

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 각 행에 대한 누적 합 계산
for i in range(N):
    for j in range(1, N):
        table[i][j] += table[i][j-1]

# 각 열에 대한 누적 합 계산
for i in range(N):
    for j in range(1, N):
        table[j][i] += table[j-1][i]

# 특정 구간의 합 계산
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
    total_sum = table[x2][y2]

    if x1:
        total_sum -= table[x1-1][y2]
    if y1:
        total_sum -= table[x2][y1-1]
    if x1 and y1:
        total_sum += table[x1-1][y1-1]

    print(total_sum)

'''
python3 : 73316KB / 1100ms
PyPy3 : 121296KB / 372ms
시간 복잡도 : O(N^2)
'''


# 시간 초과
# 시간 복잡도 : O(N*M*(y2-y1))
'''
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum(sum(part[y1-1:y2]) for part in table[x1-1:x2]))
'''