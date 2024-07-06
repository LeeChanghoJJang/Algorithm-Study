from itertools import product

def solution(N, number):
    S = [set() for _ in range(9)]

    if N == number:
        return 1
    else:
        S[1].add(N)

    for i in range(2,9):
        S[i].add(int(str(N)*i))
        for j in range(1,i):
            for x,y in product(S[j],S[i-j]):
                S[i].update({x+y,x-y,x*y})
                if y != 0:
                    S[i].add(x//y)
        if number in S[i]:
            return i
    return -1
'''
N이 1일 때는 number만큼 반복. 11이나 111같은 경우 제외
N이 2일 때는 1 2, 2 1, 3 3, 4 2, 5 4,6 3, 
'''