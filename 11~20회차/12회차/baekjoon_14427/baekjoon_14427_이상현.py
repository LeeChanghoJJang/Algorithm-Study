import sys
input = sys.stdin.readline  # 입력 속도 향상을 위해 sys.stdin.readline 사용

from heapq import *  # heapq 모듈 import

N = int(input())  # 배열의 길이 입력
list_ = list(map(int, input().split()))  # 배열 입력
M = int(input())  # 쿼리 개수 입력

q = [(list_[i], i) for i in range(N)]  # (값, 인덱스) 튜플을 힙에 저장
heapify(q)  # 힙 속성 유지

for _ in range(M):  # 쿼리 개수만큼 반복
    query, *temp = list(map(int, input().split()))  # 쿼리 입력

    if query == 1:  # 쿼리가 1인 경우
        list_[temp[0] - 1] = temp[1]  # 배열의 해당 인덱스 값을 갱신
        heappush(q, (temp[1], temp[0] - 1))  # 힙에 새로운 값을 추가
    else:  # 쿼리가 2인 경우
        while list_[q[0][1]] != q[0][0]:  # 최솟값이 배열에 있는지 확인
            heappop(q)  # 최솟값이 배열에 없으면 힙에서 제거

        print(q[0][1] + 1)  # 최솟값의 인덱스 출력
