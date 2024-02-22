import sys
sys.stdin = open('input.txt')

import heapq

def process_deletion(heap, visited):
    # 최소 힙 또는 최대 힙에서 중복된 값이 있는지 확인하고 처리하는 함수
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)
    if heap:
        visited[heap[0][1]] = False
        heapq.heappop(heap)

t = int(input())

for _ in range(t):
    k = int(input())
    q1, q2 = [], []  # 최소 힙과 최대 힙 초기화
    visited = [False] * k  # 값이 삽입되었는지 여부를 나타내는 리스트 초기화

    for j in range(k):
        com, num = input().split()

        if com == 'I':
            # 'I' 연산인 경우 최소 힙과 최대 힙에 값을 삽입하고, 해당 값이 삽입되었음을 표시
            heapq.heappush(q1, (int(num), j))
            heapq.heappush(q2, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                # 'D 1' 연산인 경우 최대 힙에서 최대값을 삭제하고, 중복된 값이 있는지 확인하여 처리
                process_deletion(q2, visited)
            else:
                # 'D -1' 연산인 경우 최소 힙에서 최소값을 삭제하고, 중복된 값이 있는지 확인하여 처리
                process_deletion(q1, visited)

    # 남은 값들 중에서 중복된 값이 있는지 확인하여 처리
    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)

    # 최종 결과 출력
    if not q1 or not q2 or not visited.count(True):
        # 어떤 힙도 비어있거나, 값이 삽입되지 않은 경우 "EMPTY" 출력
        print("EMPTY")
    else:
        # 최대값과 최소값 출력
        a = -q2[0][0]
        b = q1[0][0]
        print("%d %d" % (a, b))

