from heapq import *

N, K = map(int, input().split())
jewel_list = []

for _ in range(N):
    w, v = map(int, input().split())
    jewel_list.append([w, v])

bag_list = [int(input()) for _ in range(K)]
bag_list.sort(reverse = True)
jewel_list.sort(reverse = True)
temp = []
result = 0

while bag_list:
    bag = bag_list.pop()

    while jewel_list:
        weight, value = jewel_list.pop()

        if bag >= weight:
            heappush(temp, -value)
        else:
            jewel_list.append((weight, value))
            break

    if temp:
        result -= heappop(temp)

print(result)