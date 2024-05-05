def solution(board, moves):
    bucket = []
    N = len(board)
    cnt = 0
    for move in moves:
        move = move-1
        for i in range(N):
            if board[i][move]:
                if not bucket or bucket[-1] != board[i][move]:
                    bucket.append(board[i][move])
                    
                else:
                    bucket.pop()
                    cnt += 2
                board[i][move] = 0
                break
    
                
    answer = cnt
    return answer