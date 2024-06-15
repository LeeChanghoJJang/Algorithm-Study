import sys
sys.stdin = open('input.txt')

N = int(input())
list_ = sorted(map(int, input().split()))
min_ = 1

for w in list_:
    if min_ < w:
        break
    min_ += w

print(min_)