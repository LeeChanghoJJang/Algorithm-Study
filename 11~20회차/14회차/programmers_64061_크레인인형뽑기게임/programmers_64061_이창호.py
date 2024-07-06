def solution(board, moves):
    result = []
    count = 0
    N = len(board)
    # 각 열별로 밑에서부터 쌓기 위함.
    idx_dict = {i:[] for i in range(1,N+1)}
    # 밑에서 부터 순회
    for i in range(N-1,-1,-1):
        for j in range(N):
            # board에 숫자가 있으면
            if board[i][j]:
                # 있는 숫자만 추가시키기
                idx_dict[j+1].append(board[i][j])
    # moves에서 해당 열을 순회하면
    for move in moves:
        # 각 열에 인형이 있다면
        if idx_dict.get(move):
            # 위에서 인형을 뽑는다
            now = idx_dict[move].pop()
            # result가 있고, 마지막이 현재 뽑은거랑 같은 인형일 때만
            if result and result[-1] == now:
                # pop을 하고, count를 2회 더해준다
                result.pop()
                count+=2
                continue
            # 위에 것이 아니면 인형을 추가해준다.
            result.append(now)
    # moves를 전부 순회한 후 남은 count를 반환한다.
    return count