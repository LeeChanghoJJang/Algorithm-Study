# 7662 / 이중 우선순위 큐 / 골드4

import sys
sys.stdin = open('input.txt')

import heapq

for tc in range(int(input())):
    max_heap, min_heap = [], []
    k = int(input())
    check = [0] * k  # 삭제 원소 저장 배열

    for i in range(k):
        char, num = input().split()
        if char == 'I':
            # 인덱싱 하는 이유: 원소 동기화
            heapq.heappush(max_heap, [-int(num), i])
            heapq.heappush(min_heap, [int(num), i])
        else:
            if num == '1' and min_heap:
                check[heapq.heappop(max_heap)[1]] = 1
            elif num == '-1' and max_heap:
                check[heapq.heappop(min_heap)[1]] = 1

        # 다른 쪽에서 삭제된 원소면 삭제
        while max_heap and check[max_heap[0][1]] == 1:
            heapq.heappop(max_heap)
        while min_heap and check[min_heap[0][1]] == 1:
            heapq.heappop(min_heap)
        
    # 최댓값: 최대 힙에서 추출 / 최솟값: 최소 힙에서 추출
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
'''
288348KB / 7964ms
'''