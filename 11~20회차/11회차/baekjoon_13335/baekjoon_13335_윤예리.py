import sys
input = sys.stdin.readline
from collections import deque

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
hours = 0
bridge = deque([0] * w)

# 모든 트럭이 다리에 올라가면 코드 종료
while trucks:
    hours += 1
    bridge.popleft()

    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
# print(hours)
print(w+hours)

