import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = list(input().split())
visited = set(''.join(arr))

target = sorted(arr)
answer = -1

q = deque([arr, 0])

while q:
    lst, cnt = q.popleft()
    if lst == target:
        answer = cnt
        break

    for i in range(n-k+1):
        k_lst = lst[i:i+k]
        k_lst.reverse()
        lst2 = lst[:i] + k_lst + lst[i+k:]
        str_ = ''.join(lst2)
        if str_ not in visited:
            q.append([lst2, cnt+1])
            visited.add(str_)

print(answer)

