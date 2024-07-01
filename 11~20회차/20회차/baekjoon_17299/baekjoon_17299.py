from collections import Counter

N = int(input())
arr = [*map(int,input().split())]

counter = Counter(arr)
stack,ans = [],[-1]*N

for i in range(N):
    while stack and counter[arr[stack[-1]]] < counter[arr[i]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)