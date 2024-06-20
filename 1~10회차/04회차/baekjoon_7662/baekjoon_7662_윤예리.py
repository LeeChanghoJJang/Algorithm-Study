# import sys
# sys.stdin = open('input.txt')

import heapq
t = int(input())
for tc in range(1, t+1):
    max_h = []
    min_h = []
    K = int(input())
    visited = [1] * K

    for idx in range(K):
        char, N = map(str, input().split())
        n = int(N)

        if char == 'I':     # 삽입
            heapq.heappush(min_h, (n, idx))
            heapq.heappush(max_h, (-n, idx))

        else:
            if n == -1:      # 최소 힙
                if min_h:
                    b = heapq.heappop(min_h)
                    visited[b[1]] = 0

            elif n == 1:   # 최대 힙
                if max_h:
                    a = heapq.heappop(max_h)
                    visited[a[1]] = 0

        # 최대 힙과 최소 힙 idx 비교해서 빼줄 거 빼주기
        while max_h and visited[max_h[0][1]] == 0:   # 최대값 idx가 0이면
            heapq.heappop(max_h)
        while min_h and visited[min_h[0][1]] == 0:
            heapq.heappop(min_h)

    if min_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print('EMPTY')
