# 크레인 인형뽑기 게임 (2019 카카오 개발자 겨울 인턴십)

def solution(board, moves):
    ans = 0
    stack = []
    for j in moves:
        i = 0
        j -= 1

        # 인형 뽑기
        while i < len(board):
            if board[i][j]:
                stack.append(board[i][j])
                board[i][j] = 0
                break
            i += 1

        # 같은 인형 2개가 있다면 제거
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            ans += 2

    return ans