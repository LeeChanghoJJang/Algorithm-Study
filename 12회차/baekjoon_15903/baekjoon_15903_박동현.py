from heapq import heappop,heappush,heapify

N,M = map(int,input().split())
arr = list(map(int,input().split()))
heapify(arr)

for _ in range(M):
    a = heappop(arr)
    b = heappop(arr)
    for _ in range(2):
        heappush(arr, a+b)

print(sum(arr))