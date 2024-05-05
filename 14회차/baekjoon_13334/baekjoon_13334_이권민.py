# 사람 수, 철로의 길이 개 김
# 입력 순서대로 안옴. 위치 정수임. 
# 이진탐색? 스타트포인트랑 도착포인트. 인덱스 빼면 인원수.
# 스타트 포인트는 차례대로.


# def end_index(st,ed,length):
#     global max_cnt
    
#     if st>=ed:
#         return
#     md = (st+ed)//2
#     if n_lst[md][1] <= n_lst[st][0]+length:
#         max_cnt = max(max_cnt,md-st+1)
#         end_index(md,ed,length)
#     else:
#         end_index(st,md,length)
        
        
        
import heapq    
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
n_lst = []
for _ in range(n):
    start,end = map(int,input().split())
    if start > end:
        start,end = end, start
    n_lst.append((start,end))
    # 좌표값 낮은 거를 앞으로.
distance = int(input())
max_cnt = 0
n_lst.sort(key=lambda x: (x[1],x[0]))
# 좌표값 높은 거 기준으로 정렬. 후 앞 좌표 기준으로 오름차순
heap = []
# end_index(0,n-1,distance)

for cur in n_lst:
    st,ed = cur
    heapq.heappush(heap, st)
    st_point = ed - distance
    # 지금 애의 st_point안에 앞점이 있으면 넘어가고 아니면 pop
    while heap and heap[0] < st_point:
        heapq.heappop(heap)
    max_cnt = max(max_cnt, len(heap))
print(max_cnt)
        
    


