import sys
from math import ceil
input = sys.stdin.readline


N,K = map(int,input().split())

man = [0] * 7
woman = [0] * 7

for _ in range(N):
    gen,grade = map(int,input().split())
    if gen == 0 :
        man[grade] += 1
    elif gen == 1 :
        woman[grade] += 1

result = sum(map(lambda x : ceil(x/K), man)) + sum(map(lambda x : ceil(x/K), woman))

print(result)