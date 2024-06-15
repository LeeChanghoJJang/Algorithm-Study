import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []
max_len = 0
value = {}
for _ in range(n):
    s = deque(list(input().strip()))
    arr.append(s)
    max_len = max(max_len, len(s))

while max_len > 0:
    for i in range(n):
        if len(arr[i]) == max_len:
            char = arr[i].popleft()
            if char in value:
                value[char] += 10**(max_len-1)
            else:
                value[char] = 10**(max_len-1)
    max_len -= 1
# print(value)

num = 9
tmp = sorted(value, key=lambda x:-value[x])
answer = 0
# print(tmp)
for i in range(len(tmp)):
    # print(value[tmp[i]])
    answer += value[tmp[i]] * num
    num -= 1
print(answer)

