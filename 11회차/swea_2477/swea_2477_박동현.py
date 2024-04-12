from collections import deque

for tc in range(int(input())):

    N,M,K,A,B = map(int,input().split())
    # 접수 창구 : N 개
    # 정비 창구 : M 개
    # 방문 고객 : K 명
    # 지갑을 두고 간 고객이 이용한 접수 창구 번호 : A 
    # 지갑을 두고 간 고객이 이용한 정비 창구 번호 : B
    A,B = A-1,B-1   # 인덱스 보정
    # 접수 창구 처리 시간 : reception_time
    reception_time = list(map(int,input().split()))
    # 정비 창구 처리 시간 : repair_time
    repair_time = list(map(int,input().split()))

    # 각 고객 번호의 사람이 정비소에 도착하는 시간
    T = deque(map(int,input().split()))

    reception = [0] * N
    repair = [0] * M
    repair_ready = deque()

    A_list = [] # A 창구를 이용한 고객 리스트 
    idx = 1     # 고객번호 
    time = 0    # 시간
    ans = 0
    # 종료 조건 : 모든 사람이 다 빠질 떄 까지
    while T or any(repair) or any(reception) :
        # 접수 데스크
        for desk in range(N) :
            # 데스크가 차있으면
            if reception[desk] :
                reception[desk][1]-=1
                # 업무가 끝났으면
                if reception[desk][1] == 0 :
                    # 빼주고
                    repair_ready.append(reception[desk][0])
                    # 그 자리에 다시 넣어주기
                    if T and time >= T[0] :
                        T.popleft()
                        reception[desk] = [idx,reception_time[desk]]
                        # A 에 앉은 사람인지 체크
                        if desk == A :
                            A_list.append(idx)
                        idx += 1
                    else :
                        reception[desk] = 0 

            # 데스크가 비어있으면
            else :
                # 고객 번호의 사람이 정비소에 도착해 있다면
                if T and time >= T[0] :
                    T.popleft()
                    reception[desk] = [idx,reception_time[desk]]
                    if desk == A :
                        A_list.append(idx)
                    idx += 1
        # 정비 데스크
        for desk in range(M):
            # 데스크에 사람이 있으면
            if repair[desk] :
                repair[desk][1] -= 1
                # 정비가 끝났으면
                if repair[desk][1] == 0 :
                    # 대기자가 있으면
                    if repair_ready :
                        ready = repair_ready.popleft()
                        repair[desk] = [ready, repair_time[desk]]
                        if desk == B and ready in A_list : 
                            ans += ready
                    else :
                        repair[desk] = 0 


            # 데스크가 비어있으면 
            else :
                # 수리 대기중인 사람이 있으면 
                if repair_ready :
                    ready = repair_ready.popleft()
                    repair[desk] = [ready, repair_time[desk]]
                    if desk == B and ready in A_list :
                        ans += ready
        # 모든 과정이 끝나면 time 한칸 올리기
        time += 1
    if ans == 0 :
        ans -= 1
    print(f"#{tc+1} {ans}")