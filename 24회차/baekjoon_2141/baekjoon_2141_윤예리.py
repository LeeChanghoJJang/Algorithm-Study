import sys
input = sys.stdin.readline

n = int(input())
people = 0
arr = []    

for _ in range(n):
    pos, ple = map(int, input().split())
    arr.append((pos, ple))
    people += ple

arr.sort(key=lambda x:x[0])

cnt = 0
for pos, ple in arr:
    cnt += ple
    if cnt >= people / 2:
        print(pos)
        break