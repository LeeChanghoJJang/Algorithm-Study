import sys
sys.stdin = open('input.txt')

k = int(input())    # 1m^2 당 자라는 참외의 수
ls = []
left_right = []
up_down = []

for _ in range(6):
    direction, distance = map(int, input().split())
    ls.append([direction, distance])

for i in ls:
    if i[0] == 1 or i[0] == 2:      # 동쪽 / 서쪽
        left_right.append(i)
    else:                           # 북쪽 / 남쪽
        up_down.append(i)

max_w = max(left_right, key=lambda x : x[1])[1]
max_h = max(up_down, key=lambda x : x[1])[1]
total = max_w * max_h

here_w = []
for i in left_right:
    if i[1] == max_w:
        pass
    else:
        here_w.append(i[1])

    if sum(here_w) == max_w:
        cut_w = here_w.pop()

here_h = []
for i in up_down:
    if i[1] == max_h:
        pass
    else:
        here_h.append(i[1])

    if sum(here_h) == max_h:
        cut_h = here_h.pop()

print(here_w, here_h)
print((max_w * max_h - cut_w * cut_h)*k)


