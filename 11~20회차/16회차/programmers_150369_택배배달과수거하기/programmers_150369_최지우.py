def solution(cap, n, deliveries, pickups) :
    answer = 0

    D = 0
    P = 0
    
    for i in range(n-1, -1, -1):
        D += deliveries[i]
        P += pickups[i]
        
        while D > 0 or P > 0:
            D -= cap
            P -= cap
            answer += (i+1) * 2
    return answer