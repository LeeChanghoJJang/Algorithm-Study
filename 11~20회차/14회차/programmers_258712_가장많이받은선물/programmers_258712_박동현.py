

def solution(friends, gifts):
    answer = 0
    
    friends_idx = {k:idx for idx, k in enumerate(friends)}
    board = [[0] * len(friends) for _ in range(len(friends))]
    answer_board = [0] * len(friends)
    
    
    for gift in gifts:
        a, b  = gift.split()
        board[friends_idx[a]][friends_idx[b]] +=1
    
    
    a_list = [0] * len(friends)
    for i in range(len(board)):
        for j in range(len(board)):
            a_list[i] -= (board[j][i])
            a_list[i] += (board[i][j])

    for idx in range(len(friends)):
        for m in range(idx+1, len(friends)):
            
            if board[idx][m] < board[m][idx]:
                answer_board[m] +=1
            
            elif board[idx][m] > board[m][idx]:
                answer_board[idx] +=1
                
            else:
                if a_list[idx] > a_list[m]:
                    answer_board[idx] +=1
                    
                elif a_list[idx] < a_list[m]:
                    answer_board[m] +=1

    answer = max(answer_board)
            
    return answer