import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = [0] * 1000001
for i in arr:
    cnt[i] += 1

answer = [-1] * n
stack = []
for i in range(n):
    while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)