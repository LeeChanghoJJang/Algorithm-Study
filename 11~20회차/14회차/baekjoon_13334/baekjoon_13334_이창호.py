import sys
from heapq import *
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
home_offices = []

for _ in range(n):
    h,o = sorted(map(int,input().split()))
    heappush(home_offices,(o,h))

d= int(input()) # 허용거리
possible = []
max_val = 0
cnt = 0
while home_offices:
    # 오피스, 홈
    o,h = heappop(home_offices)
    # 홈이 오피스랑 허용거리 안에 있으면 possible에 추가한다.
    if h >= o - d:
        heappush(possible,(h,o))
        cnt+=1
    # possible에서 계속 뽑는다.
    while possible:
        # 허용거리 밖에 있는것들만 뽑는다
        start, end = heappop(possible)
        if start < o -d:
            cnt -=1
        else:
            # 마지막꺼는 다시 넣고 break
            heappush(possible,(start,end))
            break
    # 최댓값 갱신
    max_val = max(cnt,max_val)
print(max_val)