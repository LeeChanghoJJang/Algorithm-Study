# 백준 11660번 구간 합 구하기 5

n, m = map(int, input().split())
list_ = [[0] + list(map(int, input().split())) for _ in range(n)]
target = [list(map(int, input().split())) for _ in range(m)]

# 각 행별로 누적합을 미리 계산함
for row in list_:
    for i in range(n):
        row[i + 1] += row[i]

for i in range(m):
    sum_ = 0

    # target[0], target[2]는 행에 대한 정보
    # target[1], target[3]는 열에 대한 정보
    for row in range(target[i][0] - 1, target[i][2]):
        sum_ += list_[row][target[i][3]] - list_[row][target[i][1] - 1]

    print(sum_)