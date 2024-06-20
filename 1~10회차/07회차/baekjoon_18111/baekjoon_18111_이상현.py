N, M, B = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(N)]
heights = set()
result = []
sum_ = sum(sum(row) for row in list_)

for r in range(N):
    for c in range(M):
        heights.add(list_[r][c])

for height in range(min(heights), (sum_ + B)// (N * M) + 2):
    time_ = 0
    cnt = 0
    flag = False

    for r in range(N):
        for c in range(M):
            if list_[r][c] < height:
                time_ += height - list_[r][c]
                cnt += height - list_[r][c]

                if result and time_ > result[0][0]:
                    flag = True
                    break

            elif list_[r][c] > height:
                time_ += 2 * (list_[r][c] - height)
                cnt -= list_[r][c] - height

                if result and time_ > result[0][0]:
                    flag = True
                    break

        if flag:
            break

    if cnt <= B:
      result.append((time_, height))

result.sort(key = lambda x : (x[0], -x[1]))
print(*result[0])