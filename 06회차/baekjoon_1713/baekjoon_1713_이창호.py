import sys
from heapq import *
sys.stdin = open('input.txt')
# 후보 최대 인원수
N = int(input())
# 주어지는 추천번호
student_num = int(input())
# 추천번호
student_list = list(map(int,input().split()))
# 순서와 횟수를 저장하기 위해 heap으로 저장
heap = []

for idx, num in enumerate(student_list):
    # heap의 정보를 계속 갱신하기 위한 임시 heap
    tmp_heap = []
    # 기존 번호와 추천된 번호가 같을 때 여부를 판단하기 위한 변수
    flg=0
    # heap에서 모두 꺼내서, 같은 넘버가 추천된 경우가 있다면 cnt 추가하고 임시 heap에 저장
    while heap:
        cnt,old_idx,std_num = heappop(heap)
        cnt +=1 if std_num ==num else 0
        heappush(tmp_heap,(cnt,old_idx,std_num))
        flg += std_num == num
    # flg가 그대로고, tmp_heap이 N으로 꽉찼으면? 하나 빼자
    if not flg and len(tmp_heap) == N:
        heappop(tmp_heap)
    # 그리고 새로운 원소로 채워넣는거지(순서는 그대로, 횟수는 0로)
    if not flg:
        heappush(tmp_heap,(0,idx,num))
    heap = tmp_heap
# 추천번호만 저장한 리스트를 저장 
answer_list = [x[-1] for x in heap]
answer_list.sort()
print(*answer_list)
