from copy import deepcopy

t = int(input())

RGB = [list(map(int,input().split())) for _ in range(t)]

ans = float('inf')      # inf로 예외처리

for l in range(3):

    DP = deepcopy(RGB)
    # 0 번째에서 세갈래 길을 가는데, 나머지 길은 inf 로 예외 처리 해두기
    DP[0][(l+1)%3] = DP[0][(l+2)%3] = float('inf')  

    # RGB 거리 문제 긁어옴
    for i in range(1,t):
        for j in range(3):
            DP[i][j] += min(DP[i-1][(j+1)%3], DP[i-1][(j+2)%3])

    # 0번째에서 선택했던 값의 마지막 값을 inf로 예외처리
    DP[t-1][l] = float('inf')

    # 최소값 비교
    ans = min(ans,min(DP[t-1]))

# 출력
print(ans)