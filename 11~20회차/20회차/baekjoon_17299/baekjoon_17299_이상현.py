import sys
input = sys.stdin.readline

N = int(input())
list_ = list(map(int, input().split()))
result = [-1] * N
cnt = [0] * 1000001
stack = []

for n in list_:
    cnt[n] += 1

for i in range(N):
    while stack and cnt[list_[stack[-1]]] < cnt[list_[i]]:
        result[stack.pop()] = list_[i]
    stack.append(i)

print(*result)