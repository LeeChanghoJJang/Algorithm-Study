import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)
while m:
    s = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, s)
    heapq.heappush(cards, s)

    m -= 1
print(sum(cards))
