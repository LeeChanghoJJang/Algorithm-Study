import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

lst = [A[0]]

for item in A:
    if lst[-1] < item:
        lst.append(item)
    else:
        idx = bisect_left(lst, item)
        lst[idx] = item

print(len(lst))