from collections import deque

N,W,L = map(int,input().split())
# N : 트럭, W: 길이, L : 하중
trucks = deque(map(int,input().split()))

# queue 방식으로 bridge를 설정
bridge = deque([0] * W)

cnt = 0     # 단위 시간을 기록할 변수

# while 종료 조건 : trucks가 남아있지 않고, 
# bridge에 트럭이 없어 0만 남았을 경우
while trucks or sum(bridge)>0 :

    # 카운트가 지날때마다 제일 왼쪽의 값을 빼냄
    bridge.popleft()

    # 맨 앞에 대기 중인 트럭을 보내도 괜찮으면 popleft해서 실어보냄
    if trucks and sum(bridge) + trucks[0] <= L :
        bridge.append(trucks.popleft())

    # 아니면 0을 채워 길이를 유지
    else:    
        bridge.append(0)
    
    cnt += 1

print(cnt)