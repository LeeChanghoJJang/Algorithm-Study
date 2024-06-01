def solution(temperature, t1, t2, a, b, onboard):
    k = 1000 * 100
    t1 += 10
    t2 += 10
    temperature += 10
    
    # DP[i][j] : i분에 j 온도를 만들 수 있는 가장 적은 전력
    DP = [[k] * 51 for _ in range(len(onboard))] # j = 0 : -10 // = 50 : 40
    DP[0][temperature] = 0
    
    flag = 1 # 에어컨을 가동했을때 온도가 변하는 방향
    if temperature > t2 :
        flag = -1
 
    for i in range(1, len(onboard)):
        for j in range(51):
            arr = [k]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                # 1. 에어컨을 키지 않고 실외온도와 달라서 실내온도가 -flag 되는 경우
                if 0 <= j+flag <= 50 :
                    arr.append(DP[i-1][j+flag])
                # 2. 에어컨을 키지 않고 현재온도 j 가 실외온도랑 같아서 변하지 않는 경우
                if j == temperature:
                    arr.append(DP[i-1][j])
                # 3. 에어컨을 키고 현재온도가 변하는 경우
                if 0 <= j-flag <= 50:
                    arr.append(DP[i-1][j-flag] + a)
                # 4. 에어컨을 키고 현재온도가 희망온도라서 온도가 변하지 않는경우
                if t1 <= j <= t2:
                    arr.append(DP[i-1][j] + b)

                DP[i][j] = min(arr)
            
    answer = min(DP[len(onboard)-1])
    return answer