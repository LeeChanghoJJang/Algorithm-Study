from heapq import heappush, heappop

dx = [0, 1,-1, 1,-1, 0, 1, -1]
dy = [1, 1, 1, 0, 0, -1,-1,-1]
# dt 0 1 2 는 cost가 0 
# 나머지는 cost 1

N,M = map(int,input().split())
#

# 입력을 받으면서 정보 저장
maps = []
for idx in range(N):
    tmp = list(input())
    if "K" in tmp :
        bi,bj = (idx,tmp.index("K"))
    if "*" in tmp :
        ti,tj = (idx,tmp.index("*"))
    maps.append(tmp)

distance = [[float('inf')]*M for _ in range(N)]

hq = [(0,bi,bj)]
distance[bi][bj] = 0

while hq :
    dist_now, i,j = heappop(hq)

    if distance[i][j] >= dist_now :

        for dt in range(8): 
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < N and 0 <= dj < M and maps[di][dj] !="#" :
                if dt > 2 :
                    weight = 1
                else :
                    weight = 0 
                cost = dist_now + weight
                if distance[di][dj] > cost:
                    distance[di][dj] = cost
                    heappush(hq,(cost,di,dj))
if distance[ti][tj] == float('inf') :
    print(-1)
else :
    print(distance[ti][tj])