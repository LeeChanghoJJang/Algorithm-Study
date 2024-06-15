import sys
input = sys.stdin.readline

n = int(input())
weight = sorted(list(map(int, input().split())))

target = 1
for w in weight:
    if target < w:
        break
    target += w

print(target)
