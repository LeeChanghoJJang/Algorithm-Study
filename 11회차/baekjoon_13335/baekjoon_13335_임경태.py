# 13335 트럭

from collections import deque

# 트럭 수, 다리 길이, 다리의 최대 하중
N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = deque([0] * W, maxlen=W)  # 최대값을 가지는 큐 생성

trucks.reverse()
load = 0
time = 0

while trucks or load:
    time += 1
    load -= bridge.popleft()

    if not trucks: continue

    # 트럭이 다리에 올라갔을 때 최대 하중을 넘지 않는다면 추가
    if load + trucks[-1] <= L:
        bridge.append(trucks.pop())
        load += bridge[-1]
    else:
        bridge.append(0)

print(time)