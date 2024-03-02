import sys
sys.stdin = open('input.txt')

K = int(input())
d, l = zip(*[list(map(int, input().split())) for _ in range(6)])
cnt = [d.count(i) for i in range(5)]
area, sub_area = 1, 1

for i in range(6):
    if cnt[d[i]] == 1:
        area *= l[i]
    elif d[(i - 1) % 6] == d[(i + 1) % 6]:
        sub_area *= l[i]

print(K*(area - sub_area))