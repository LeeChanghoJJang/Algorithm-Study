def solution(coin, cards):
    co = coin
    life = 0
    answer = 0
    n = len(cards)
    exist_card = [0] * (n+1) # 1 최초 소지 카드
    possible_card =  [0] * (n+1) # 사지는 않았지만 나왔던 것, life < 0 이되는 순간 정리 (일단 1개)
    possible_life = 0
    r = 0
    
    for i in range(0,int(n/3)):
        exist_card[cards[i]] = 1
        if exist_card[n-cards[i]+1]:
            life += 1
    
    while life >= 0:
        r += 1
        if int(n/3 + 2*r -1) >=n: # 뽑을 것 없을 때
            return r
            break
        nc1, nc2= cards[int(n/3+2*r-2)], cards[int(n/3+2*r-1)]
        if  exist_card[n + 1 - nc1]:
            if co >= 1:
                co -= 1
                life += 1    
        else:
            if possible_card[n + 1 - nc1]:
                possible_life += 1
            else:
                possible_card[nc1] = 1
        
        if  exist_card[n + 1 - nc2]:
            if co >= 1:
                co -= 1
                life += 1    
        else:
            if possible_card[n + 1 - nc2]:
                possible_life += 1
            else:
                possible_card[nc2] = 1
        
        life -= 1
        
        if life < 0 and possible_life >= 1:
            if co >= 2:
                co -=2
                life += 1
                possible_life -= 1
        
    
    return r