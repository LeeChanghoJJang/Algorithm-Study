N = int(input())
list_ = [tuple(map(int, input().split())) for _ in range(N)]
list_.sort(key = lambda x : x[0])
max1 = max(list_, key = lambda x : x[1])

prev = list_[0]
area = 0

for i, h in list_:
    if i > max1[0]:
        break
    if h > prev[1]:
        area += prev[1] * (i - prev[0])
        prev = (i, h)

list_.reverse()
prev = list_[0]
max2 = max(list_, key = lambda x : x[1])

for i, h in list_:
    if i < max2[0]:
        break
    if h > prev[1]:
        area += prev[1] * (prev[0] - i)
        prev = (i, h)

print(area + (max2[0] - max1[0] + 1) * max1[1])