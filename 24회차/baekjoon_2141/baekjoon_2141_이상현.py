N = int(input())
list_ = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
sum_ = sum(town[1] for town in list_)

cnt = 0
for i in range(N):
    cnt += list_[i][1]

    if 2 * cnt >= sum_:
        print(list_[i][0])
        break