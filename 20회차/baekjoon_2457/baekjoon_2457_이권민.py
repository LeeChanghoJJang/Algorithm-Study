import sys

n = int(sys.stdin.readline())
date = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    date.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])

date.sort(key=lambda x:(x[0], x[1]))
cnt = 0
end = 0
target = 301

while date:
    if target >= 1201 or target < date[0][0]:
        break

    for _ in range(len(date)):
        if target >= date[0][0]:
            if end <= date[0][1]:
                end = date[0][1]

            date.remove(date[0])

        else:
            break

    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)