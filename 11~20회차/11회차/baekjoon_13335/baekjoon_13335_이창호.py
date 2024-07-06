import sys
from collections import deque
sys.stdin = open('input.txt')  # 입력을 파일에서 읽도록 설정

# n: 트럭의 수, w: 다리의 길이, L: 다리의 최대 하중
n, w, L = map(int, input().split())

# 트럭의 무게를 입력 받음
trucks = deque(map(int, input().split()))

# 다리 위에 올라간 트럭들의 무게의 합을 저장할 변수 초기화
temp_sum = 0

# 다리 위의 트럭을 나타내는 deque 초기화
result = deque([0] * w)

# 경과 시간을 나타내는 변수 초기화
time = 0

# 모든 트럭이 다리를 건널 때까지 반복
while trucks or sum(result) != 0:
    temp_sum -= result.popleft()  # 다리를 건너는 트럭 중 가장 먼저 들어간 트럭의 무게를 빼줌
    if trucks and temp_sum + trucks[0] <= L:  # 다음 트럭이 다리에 올라갈 수 있는지 확인
        temp_sum += trucks[0]  # 다음 트럭을 다리에 올리고 다리 위 트럭들의 무게의 합을 업데이트
        result.append(trucks.popleft())  # 다음 트럭을 다리 위에 올림
    else:
        result.append(0)  # 다음 트럭이 올라가지 못하면 다리 위에는 아무것도 올리지 않음
    time += 1  # 경과 시간을 증가
print(time)  # 걸린 시간 출력
