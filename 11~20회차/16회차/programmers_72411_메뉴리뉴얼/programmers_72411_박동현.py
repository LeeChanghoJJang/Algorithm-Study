from itertools import combinations 
from collections import Counter

def solution(orders, course):
    answer = [] 
    comb = []
    for order in orders:
        for c in course:
            comb += combinations(sorted(order), c)
    
    ct = Counter(comb).most_common()
    
    rest = {}
    for key, value in ct:
        if len(key) not in rest.keys() or rest[len(key)] == value:
            if value <= 1: break
            answer.append(''.join(key))
            rest[len(key)] = value

    return sorted(answer)