import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
hq = []

# for _ in range(N):
#     arr = list(map(int,input().split()))
#     for num in arr :
#         heappush(hq, -num)

# for _ in range(N):
#     ans = heappop(hq)

# print(-ans)
### 전체를 저장해서 최대힙으로 구성하는 경우 메모리 초과 발생


### 최소힙을 사용, 리스트의 길이를 최대 N으로 제한하여 구성
#### 제한된 길이의 가장 앞 요소가 N번째로 큰 수가 됨

for _ in range(N):
    arr = list(map(int,input().split()))
    for item in arr :
        heappush(hq,item)
        if len(hq) > N:
            heappop(hq)
print(hq[0])