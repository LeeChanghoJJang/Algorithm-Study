from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_ = -1

    for comb in combinations_with_replacement(range(11), n):
        info_peach = [0] * 11
        lion = peach = 0
        
        for score in comb:
            info_peach[10 - score] += 1
            
        for score in range(11):
            if info[score] == info_peach[score] == 0:
                continue
            if info[score] >= info_peach[score]:
                peach += 10 - score
            else:
                lion += 10 - score
                
        if lion <= peach:
            continue
        
        if lion - peach > max_:
            max_ = lion - peach
            answer = info_peach

    return answer