import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [[0] * 100 for _ in range(100)]
for i in range(n):
    a1, a2 = map(int, input().split())

    for i in range(a1, a1+10):
        for j in range(100-a2-10, 100-a2):
            arr[i][j] = 1

total = 0
for i in arr:
    total += sum(i)

print(total)