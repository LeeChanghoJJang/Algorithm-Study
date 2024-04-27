import sys
sys.stdin = open('input.txt')
from itertools import combinations

total = []
for _ in range(9):
    i = int(input())
    total.append(i)
two = list(combinations(total, 2))
for j in two:
    if sum(j) == (sum(total)-100):
        total.pop(total.index(j[0]))
        total.pop(total.index(j[1]))
print(*sorted(total), sep='\n')