import sys
input = sys.stdin.readline

N,M = map(int,input().split())

LAN = [int(input()) for _ in range(N)]


left = 1                    # 최소 길이 1
right = max(LAN)            # 최대 길이 max

while left <= right:        # 둘이 붙을 때 까지
    mid = (left+right)//2   # 이분탐색
    cnt = 0

    for i in LAN:           # 각 랜선에 대해
        cnt += i//mid       # 중앙값으로 나눈 몫을 cnt에 더해줌 

    if cnt >= M:            # 만약 같거나 크거나 같으면
        left = mid+1        # left를 올려 다시 시행
        result = mid        # 같은 경우 result 인 경우도 있으니 저장

    else:                   # cnt가 더 낮으면
        right = mid-1       # 최대값을 낮춰서 다시 탐색

print(result)