# 2477 차량 정비소

from collections import deque

class Guest:
    def __init__(self, pk):
        self.pk = pk
        self.numA = 0
        self.numB = 0
        self.time = 0
        self.end = False

def find(arr, V):
    try: return arr.index(V)
    except ValueError: return -1

for tc in range(int(input())):
    N, M, K, A, B = map(int, input().split())  # 접수 창구 수, 정비 창구 수, 방문 고객 수, 타겟 접수 창구, 타겟 정비 창구
    timeA = list(map(int, input().split()))  # 접수 소요 시간 : N개
    timeB = list(map(int, input().split()))  # 정비 소요 시간 : M개
    timeT = list(map(int, input().split()))  # 고객 방문 시간 : K개

    deskA = [False] * N; waitA = deque([])  # 접수 창구 및 대기
    deskB = [False] * M; waitB = deque([])  # 정비 창구 및 대기

    timeT = deque(timeT)
    ans, num = 0, 1
    guests = []

    for t in range(5000):
        # 정비 창구
        for j, desk in enumerate(deskB):
            if not(desk and not desk.time): continue

            # 정비 대기 인원 정비 창구 이동
            if waitB:
                deskB[j] = waitB.popleft()
                deskB[j].time = timeB[j]
                deskB[j].numB = j
            else:
                deskB[j] = False
            # 종료 조건 추가
            desk.end = True

        # 접수 창구
        for i, desk in enumerate(deskA):
            if not desk or desk.time > 0: continue

            # 접수 완료자 정비 창구 또는 정비 대기 이동
            j = find(deskB, False)
            if j > -1:
                deskB[j] = desk
                deskB[j].time = timeB[j]
                deskB[j].numB = j
            else:
                waitB.append(desk)

            # 접수 대기 인원 접수 창구 이동
            if waitA:
                deskA[i] = waitA.popleft()
                deskA[i].time = timeA[i]
                deskA[i].numA = i
            else:
                deskA[i] = False

        # 정비소 방문
        while timeT and timeT[0] == t:
            guests.append(Guest(num))
            # 방문자 접수 창구 또는 접수 대기 이동
            i = find(deskA, False)
            if i > -1:
                deskA[i] = guests[-1]
                deskA[i].time = timeA[i]
                deskA[i].numA = i
            else:
                waitA.append(guests[-1])

            num += 1
            timeT.popleft()

        # 시간 경과
        flag = 0
        for guest in guests:
            guest.time -= 1
            if guest.end: flag += 1

        if flag == K: break

    # 지갑 분실자 체크
    for guest in guests:
        if guest.numA == A-1 and guest.numB == B-1:
            ans += guest.pk

    print(f'#{tc+1} {ans if ans else -1}')