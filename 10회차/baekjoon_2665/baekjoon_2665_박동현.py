from heapq import *

dx,dy = [1,0,-1,0], [0,1,0,-1]

# 입력
size = int(input())
maze = [list(map(int, list(input()))) for _ in range(size)]

# 처리

q = [(0,0,0)]
distance = [[float('inf')]*size for _ in range(size)]
distance[0][0] = 0
# 0이면 거리 +1 1이면 거리 + 0
while q :
    dist_now, i, j = heappop(q)

    if distance[i][j] >= dist_now :
        for dt in range(4):
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < size and 0 <= dj < size:
                cost = dist_now + 1 - maze[di][dj]
                if distance[di][dj] > cost :
                    distance[di][dj] = cost
                    heappush(q,(cost,di,dj))

print(distance[size-1][size-1])