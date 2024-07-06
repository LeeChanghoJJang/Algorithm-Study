# 인형 뽑기

def solution(board, moves):
    answer = 0
    stack = []
    length = len(board)
    for move in moves:
        check = False
        move-=1
        i=0
        while not board[i][move]:
            i += 1
            if i == length :
                check = True
                break
        if check :
            continue
            
        doll = board[i][move] 
        board[i][move] = 0        

        if stack and doll == stack[-1]:
            stack.pop()
            answer+=2
        else :
            stack.append(doll)
    return answer