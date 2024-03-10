import sys
from heapq import *
sys.stdin = open('input.txt')

N = int(input())
student_num = int(input())
student_list = list(map(int,input().split()))
heap = []

for idx, num in enumerate(student_list):
    tmp_heap = []
    flg=0
    while heap:
        cnt,old_idx,std_num = heappop(heap)
        cnt +=1 if std_num ==num else 0
        heappush(tmp_heap,(cnt,old_idx,std_num))
        flg += std_num == num

    if not flg and len(tmp_heap) >= N:
        heappop(tmp_heap)

    if not flg:
        heappush(tmp_heap,(0,idx,num))
    heap = tmp_heap

answer_list = [x[-1] for x in heap]
answer_list.sort()
print(*answer_list)