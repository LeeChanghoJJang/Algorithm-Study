import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
# 원래 순서와 뽑은 번호를 순차적으로 저장
queue = deque(map(int,input().split()))
orders= []
# 순차적으로 앞부터 순회 
for i in range(1,T+1):
    num = queue.popleft()
    # 만약 num이 0이면 맨끝 그대로
    if num == 0:
        orders.append(i)
    # num이 0이 아니면 뽑은 만큼 앞으로 가야함
    else:
        orders.insert(i-num-1,i)
print(*orders)
