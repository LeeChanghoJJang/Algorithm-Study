def solution(friends, gifts):
    N = len(friends)

    gift_table = [[0] * N for _ in range(N)]
    gift_score_table = [[0] * 2 for _ in range(N)]
    dict_ = {friends[i]: i for i in range(N)}
    result = [0] * N

    for gift in gifts:
        give, receive = gift.split()
        gift_table[dict_[give]][dict_[receive]] += 1

    for row in range(N):
        gift_score_table[row][0] = sum(gift_table[row])
        gift_score_table[row][1] = sum(gift_table[i][row] for i in range(N))

    for i in range(N - 1):
        for j in range(i + 1, N):
            if gift_table[i][j] > gift_table[j][i]:
                result[i] += 1
            elif gift_table[i][j] < gift_table[j][i]:
                result[j] += 1
            else:
                if gift_score_table[i][0] - gift_score_table[i][1] > gift_score_table[j][0] - gift_score_table[j][1]:
                    result[i] += 1
                elif gift_score_table[i][0] - gift_score_table[i][1] < gift_score_table[j][0] - gift_score_table[j][1]:
                    result[j] += 1

    answer = max(result)
    return answer