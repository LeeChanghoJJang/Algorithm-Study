def solution(numbers, hand):
    key_pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    L = [3,0]
    R = [3,2]
    answer = ''
    for number in numbers:
        for i in range(4):
            for j in range(3):
                if number == key_pad[i][j]:
                    if number in [2,5,8,0]:
                        if abs(L[0]-i)+abs(L[1]-j) > abs(R[0]-i)+abs(R[1]-j):
                            R = [i,j]
                            answer += 'R'
                        elif abs(L[0]-i)+abs(L[1]-j) < abs(R[0]-i)+abs(R[1]-j):
                            L = [i,j]
                            answer += 'L'
                        else:
                            if hand == 'right':
                                R = [i,j]
                                answer += 'R'
                            else:
                                L = [i,j]
                                answer += 'L'
                    elif number in [1,4,7]:
                        L = [i,j]
                        answer += 'L'
                    else :
                        R = [i,j]
                        answer += 'R'
                        
    
    return answer