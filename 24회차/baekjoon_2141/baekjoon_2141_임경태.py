# 2141 우체국
N = int(input())
location = []
p = 0

# 각 위치와 가중치를 입력받음
for i in range(1, N + 1):
    a, b = map(int, input().split())
    location.append((a, b))
    p += b  # 가중치의 합을 계산

# 위치를 기준으로 정렬
location.sort(key=lambda x: x[0])

# 중간 위치를 찾기 위한 변수 초기화
cnt = 0

# 위치를 순회하며 중간 위치를 찾음
for i in range(N):
    cnt += location[i][1]  # 현재까지의 가중치 합
    if cnt >= p / 2:  # 현재까지의 가중치 합이 총 가중치 합의 절반 이상인 경우
        print(location[i][0])  # 해당 위치를 출력
        break
