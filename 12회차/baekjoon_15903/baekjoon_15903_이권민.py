# 차이가 적은 애들끼리 더해야.
from heapq import heappush,heappop,heapify
n,m = map(int,input().split())
num_lst = list(map(int,input().split()))
# 정렬한다음에
heapify(num_lst)
for _ in range(m):
    a = heappop(num_lst)
    b = heappop(num_lst)
    c = a+b
    heappush(num_lst,c)
    heappush(num_lst,c)
print(sum(num_lst))
