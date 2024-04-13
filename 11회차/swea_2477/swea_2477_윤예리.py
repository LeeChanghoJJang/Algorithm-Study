import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, m, k, a, b = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    tk = [0] + list(map(int, input().split()))
    customer_idx = 1
    
    # reception 대기
    waiting1 = deque()
    # repair 대기
    waiting2 = deque()

    # 다녀갔던 사람들 저장
    receptions = [[] for _ in range(n)]
    reception_cnt = 0
    repairs = [[] for _ in range(m)]
    repair_cnt = 0

    t = 0
    result = 0

    while not(customer_idx > k and reception_cnt == 0 and repair_cnt == 0):
        # 도착한 손님 reception 대기
        for i in range(customer_idx, k+1):
            if customer_idx <= k and tk[customer_idx] <= t:
                waiting1.append(customer_idx)
                customer_idx += 1
            else:
                break

        # waiting2
        for i in range(n):
            if receptions[i]:
                num, enter = receptions[i]
                if t-enter >= ai[i]:
                    receptions[i] = []
                    reception_cnt -= 1
                    waiting2.append([num, i+1])

        # waiting1
        for i in range(n):
            if not waiting1 or reception_cnt == n:
                break
            if not receptions[i]:
                num = waiting1.popleft()
                receptions[i] = [num, t]
                reception_cnt += 1

        # waiting2
        for i in range(m):
            if repairs[i]:
                num, enter = repairs[i]
                if t-enter >= bj[i]:
                    repairs[i] = []
                    repair_cnt -= 1

        # repair
        for i in range(m):
            if not waiting2 or repair_cnt == m:
                break
            if not repairs[i]:
                num, desk_num = waiting2.popleft()
                if i+1 == b and desk_num == a:
                    result += num
                repairs[i] = [num, t]
                repair_cnt += 1

        t += 1

    if result == 0:
        result = -1
    print(result)

