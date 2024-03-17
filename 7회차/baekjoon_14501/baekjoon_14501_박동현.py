N = int(input())

DP = [0]*(N+6)                                      # 상담은 최대 5일, 첫 날 표시용 +1 해서 +6

for day in range(1,N+1):
    T,P = map(int,input().split())                  # T : 소요일,  P : 가치

    DP[day+T-1] = max(P, DP[day-1]+P,DP[day+T-1])   # 각각의 상담을 마친 날에 얻을 수 있는 가치의 최대값 계산
    DP[day] = max(DP[day-1], DP[day])               # 각각의 전날 얻을 수 있었던 최대값과 비교

print(DP[N])                                        # N일차의 값을 출력