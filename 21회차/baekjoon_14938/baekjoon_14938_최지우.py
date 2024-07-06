from heapq import heappush, heappop


def dijkstra(v):
    que = [(0, v)]
    wei = [float("INF")] * (n+1)
    wei[v] = 0
    cnt = items[v-1]
    while que:
        now_w, now = heappop(que)
        for nxt_w, nxt in link[now]:
            new_w = now_w + nxt_w
            
            if wei[nxt] <= new_w:
                continue
            
            if new_w > m:
                continue
            
            if wei[nxt] == float("INF"):
                cnt += items[nxt-1]
            
            wei[nxt] = new_w
            heappush(que, (new_w, nxt))
            
    return cnt

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
link = {i:[] for i in range(1, n+1)}

for _ in range(r):
    s, e, w = map(int, input().split())
    link[s].append((w, e))
    link[e].append((w, s))

result = 0
for i in range(1, n+1):
    result = max(dijkstra(i), result)
    
print(result)