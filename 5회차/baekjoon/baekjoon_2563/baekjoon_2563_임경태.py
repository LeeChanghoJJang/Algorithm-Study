import sys
sys.stdin = open('input.txt')

N = int(input())
paper = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

cnt = 0
for p in paper:
    cnt += p.count(1)

print(cnt)