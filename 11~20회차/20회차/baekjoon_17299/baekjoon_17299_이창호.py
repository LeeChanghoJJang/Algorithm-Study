from collections import Counter
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))
num_cnt = Counter(arr)
result = [-1] * N
stack = [0]

for i in range(N):
    while stack and num_cnt[arr[stack[-1]]] < num_cnt[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)