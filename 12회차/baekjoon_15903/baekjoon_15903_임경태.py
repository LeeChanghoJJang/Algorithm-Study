# 15903 카드 합체 놀이

from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
nums = list(map(int, input().split()))
heapify(nums)

for _ in range(m):
    # 최솟값 두 수 호출
    a = heappop(nums)
    b = heappop(nums)

    # 합산 후 저장
    c = a + b
    heappush(nums, c)
    heappush(nums, c)

print(sum(nums))