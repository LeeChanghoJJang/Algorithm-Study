import sys
from collections import deque
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    '''
        접수창구의 수 : N (1~9)
        정비창구의 수 : M (1~9)
        차량정비소 방문 고객수 : K (2~1000)
        지갑을 두고 간 고객이 이용한 접수 창구번호 : A
        지갑을 두고 간 고객이 이용한 정비 창구번호 : B
    
        1. 빈 접수 창구가 있는 경우, 빈 접수 창구에 가서 고장 접수
        2. 빈 접수 창구가 없는 경우, 빈 접수 창구 생길 때까지 대기
        3. 빈 정비 창구가 있는 경우, 빈 정비 창구에 가서 차량을 정비
        4. 빈 정비 창구가 없는 경우, 빈 정비 창구가 생길 때까지 대기
        
        접수창구 우선순위
        1. 여러 고객 웨이팅 시, 고객번호 낮은 순서대로 우선접수
        2. 빈 창구 여러곳일 경우, 접수 창구번호가 적은 곳으로
        
        정비창구 우선순위
        1. 먼저 기다리는 고객 우선
        2. 두명이상 고객이 접수창구에서 동시 접수완료후, 정비창구로 이동한 경우, 이용했던 접수창구번호가 적은 고객 우선
        3. 빈 창구가 여러 곳인 경우, 정비 창구번호가 작은 곳으로
    '''
    N, M, K, A, B = map(int,input().split())
    # 창구별 접수 시간
    reception_cost = list(map(int,input().split()))
    # 창구별 정비 시간
    engineer_cost = list(map(int,input().split()))
    # 고객들 도착시간
    customers_waitings_time = deque(enumerate(map(int,input().split())))
    customers_index = 0
    customers_length = len(customers_waitings_time)

    # 방문 기록 저장 배열 (0번 접수창구, 1번 정비창구)
    visitor_info = [[-1,-1] for _ in range(K)]

    # 대기실에 아무도 없는 상황을 초기값
    # 인덱스 : 창구 / 0번째 값 : 고객번호 / 1번째 값 : 시간
    reception_desks = [-1] * N
    repair_desks = [-1] * M

    reception_waiting_line = deque([])
    repair_waiting_line = deque([])

    time = 0

    while 1:
        # 0. 정비 창구에서 볼일 다 본 사람 (시간이 다된 사람)
        for i in range(M):
            if repair_desks[i] != -1 and repair_desks[i][1]==0:
                repair_desks[i] = -1
        # 1. 접수 창구에서 볼일 다 본 사람 -> 정비창구 대기열로 옮기기
        for i in range(N):
            if reception_desks[i] != -1 and reception_desks[i][1] ==0:
                repair_waiting_line.append(reception_desks[i][0])
                # 해당 접수창구 초기화시켜서 다시 올수 있게끔
                reception_desks[i]=-1
        # 2. 이번 시간에 들어온 사람 '접수 창구 대기열'로 옮기기
        while customers_waitings_time and customers_waitings_time[0][1] == time:
            customer_idx, customer_time = customers_waitings_time.popleft()
            reception_waiting_line.append(customer_idx)
        # 3. 정비 창구 비어있는 곳에 대기열 사람 옮기기
        for i in range(M):
            if repair_desks[i] == -1 and repair_waiting_line:
                visitor_idx = repair_waiting_line.popleft()
                repair_desks[i] = [visitor_idx,engineer_cost[i]-1]
                # 몇번 정비 창구 방문했는지 기록하기
                visitor_info[visitor_idx][1] = i
            # 5. 정비 창구에 있는 사람 시간 -1해주기 (0되면 나감)
            elif repair_desks[i] != -1:
                repair_desks[i][1] -= 1
        # 4. 접수 창구 비어있는 곳에 대기열 사람 옮기기
        for i in range(N):
            if reception_desks[i] == -1 and reception_waiting_line:
                visitor_idx = reception_waiting_line.popleft()
                reception_desks[i] = [visitor_idx,reception_cost[i]-1]
                # 몇번 접수 창구 방문했는지 기록하기
                visitor_info[visitor_idx][0] = i
            # 5. 접수 창구에 있는 사람 시간 -1해주기 (0되면 나감)
            elif reception_desks[i] != -1:
                reception_desks[i][1] -=1

        time +=1
        if not customers_waitings_time:
            if all(visitor[1] != -1 for visitor in visitor_info):
                break

    answer = sum(1 + i for i in range(K) if visitor_info[i][0] == A - 1 and visitor_info[i][1] == B - 1)
    print(f'#{tc} {answer if answer else -1}')