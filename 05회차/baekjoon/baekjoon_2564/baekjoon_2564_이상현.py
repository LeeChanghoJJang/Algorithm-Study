def dist_(d, pos):
    if d == 1:
        return h + pos
    if d == 2:
        return 2 * (h + w) - pos
    if d == 3:
        return h - pos
    return w + h + pos

w, h = map(int, input().split())
cnt = int(input())
list_ = []
sum_ = 0

for _ in range(cnt + 1):
    d, pos = map(int, input().split())
    list_.append(dist_(d, pos))

for i in range(cnt):
    cw = abs(list_[-1] - list_[i])
    ccw = 2 * (w + h) - cw
    sum_ += min(cw, ccw)

print(sum_)