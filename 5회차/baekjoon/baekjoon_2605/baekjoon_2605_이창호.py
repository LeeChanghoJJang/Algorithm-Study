import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
queue = deque(map(int,input().split()))
orders= []
for i in range(1,T+1):
    num = queue.popleft()
    if num == 0:
        orders.append(i)
    else:
        orders.insert(i-num-1,i)
print(*orders)
