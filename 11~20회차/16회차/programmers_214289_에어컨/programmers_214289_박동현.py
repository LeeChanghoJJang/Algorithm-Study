def solution(temperature, t1, t2, a, b, onboard):
    if temperature > t2:
        tmp = temperature - t2
    else :
        tmp = t1 - temperature

    DP = [[float('inf')]*(tmp+1)+[0]]

    idx = 0
    for i in range(1, len(onboard)):
        arr = []
        for j in range(tmp+2):
            temp = [DP[i-1][j]+b]

            if j == tmp + 1:
                temp.append(DP[i-1][j])
            if j <= tmp:
                temp.append(DP[i-1][j+1] + a)
            if j > 0:
                temp.append(DP[i-1][j-1])
            
            min_cost = min(temp)

            if onboard[i] == 1:
                idx = i
                if j > 1:
                    min_cost = float('inf')
            arr.append(min_cost)

        DP.append(arr)

    return min(DP[idx])