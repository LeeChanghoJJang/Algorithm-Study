def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    for i in moves:
        i -= 1
        h = 0
        while h <= N - 1 and board[h][i] == 0:
            h += 1

        if h == N:
            continue

        pick = board[h][i]
        board[h][i] = 0

        if stack and stack[-1] == pick:
            answer += 2
            stack.pop()
        else:
            stack.append(pick)

    print(answer)
    return answer

