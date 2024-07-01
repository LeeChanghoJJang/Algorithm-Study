import sys
input = sys.stdin.readline

from itertools import permutations

k = int(input())
inequalities = input().split()
max_ = 0
min_ = float('inf')

p_list = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k + 1)

for p in p_list:
    flag = True

    for i in range(k):
        if inequalities[i] == '<':
            if p[i] < p[i + 1]:
                continue
            flag = False
            break
        else:
            if p[i] > p[i + 1]:
                continue
            flag = False
            break

    if not flag:
        continue

    p = int(''.join(map(str, p)))
    max_ = max(max_, p)
    min_ = min(min_, p)

max_, min_ = str(max_), str(min_)

if len(max_) == k:
    max_ = '0' + max_

if len(min_) == k:
    min_ = '0' + min_

print(max_)
print(min_)