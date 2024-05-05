# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    answer = []
    
    today = [*map(int,today.split("."))]
    term = dict()
    
    for trm in terms:
        t,d = trm.split()
        term[t] = int(d)
    
    for i in range(len(privacies)) :
        privacy = privacies[i]
        day,t = privacy.split()
        day = [*map(int,day.split("."))]
    
        day[1] += term[t]
        while day[1] > 12:
            day[0] += 1
            day[1] -= 12
    
        check=False

        if today[0] > day[0] :
            check = True
        elif today[0] == day[0] and today[1] > day[1] :
            check = True
        elif today[0] == day[0] and today[1] == day[1] and today[2] >= day[2] :
            check = True
            
        if check : answer.append(i+1)
    return answer