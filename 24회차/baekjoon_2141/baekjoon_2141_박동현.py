# 그냥 중앙값 구하는 문제였습니다.
import sys
input = sys.stdin.readline


arr = sorted([[*map(int,input().split())] for _ in range(int(input()))])
s,d = sum(map(lambda x: x[1], arr))+1,0
for a,b in arr:
    d += b
    if d >= s//2: exit(print(a))