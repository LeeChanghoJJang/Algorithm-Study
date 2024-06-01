# 에어컨 (2023 현대모비스 알고리즘 경진대회 예선)

def solution(temperature, t1, t2, a, b, onboard):
    N = len(onboard)
    temperature += 10
    t1 += 10
    t2 += 10

    DP = [[100000] * 51 for _ in range(N)]
    DP[0][temperature] = 0
    
    flag = 1 if temperature <= t2 else -1
 
    for i in range(1, N):
        for j in range(51):
            arr = [100000]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                # 에어컨을 키지 않고 실외온도와 달라서 실내온도가 -flag 되는 경우
                if 0 <= j+flag <= 50 :
                    arr.append(DP[i-1][j+flag])
                # 에어컨을 키지 않고 현재온도 j 가 실외온도랑 같아서 변하지 않는 경우
                if j == temperature:
                    arr.append(DP[i-1][j])
                # 에어컨을 키고 현재온도가 변하는 경우
                if 0 <= j-flag <= 50:
                    arr.append(DP[i-1][j-flag] + a)
                # 에어컨을 키고 현재온도가 희망온도라서 온도가 변하지 않는경우
                if t1 <= j <= t2:
                    arr.append(DP[i-1][j] + b)

                DP[i][j] = min(arr)

    answer = min(DP[N-1])
    return answer