def solution(coin, cards):
    coin = coin
    life = 0
    n = len(cards)
    exist_card = [0] * (n+1) 
    possible_card =  [0] * (n+1) 
    possible_life = 0
    answer = 0
    
    for i in range(0,int(n/3)):
        exist_card[cards[i]] = 1
        if exist_card[n-cards[i]+1]:
            life += 1
    
    while life >= 0:
        answer += 1
        if int(n/3 + 2*answer -1) >=n:
            return answer

        nc1, nc2= cards[int(n/3+2*answer-2)], cards[int(n/3+2*answer-1)]
        if  exist_card[n + 1 - nc1]:
            if coin >= 1:
                coin -= 1
                life += 1    
        else:
            if possible_card[n + 1 - nc1]:
                possible_life += 1
            else:
                possible_card[nc1] = 1
        
        if  exist_card[n + 1 - nc2]:
            if coin >= 1:
                coin -= 1
                life += 1    
        else:
            if possible_card[n + 1 - nc2]:
                possible_life += 1
            else:
                possible_card[nc2] = 1
        
        life -= 1
        
        if life < 0 and possible_life >= 1:
            if coin >= 2:
                coin -=2
                life += 1
                possible_life -= 1
        
    return answer