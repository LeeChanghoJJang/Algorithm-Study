def solution(n, info):
    answer = [-1]
    score = [0] * 11
    max_gap = 0

    def count_gap(score):
        ap = 0
        ry = 0

        for  i in range(len(info)):
            if info[i] > 0 or score[i] > 0:
                if info[i] >= score[i]:
                    ap += (10-i)
                else:
                    ry += (10-i)
        return (ry > ap, abs(ap-ry))

    def dfs(l, cnt):
        global max_gap, answer
        if l == 11 or cnt == 0:
            is_winner, gap = count_gap(score)
            if is_winner:
                if cnt >= 0:
                    score[10] = cnt

                if gap > max_gap:
                    max_gap = gap
                    answer = score.copy()
                elif gap == max_gap:
                    for i in range(len(score)):
                        if answer[i] > 0:
                            i_1 = i
                        if score[i] > 0:
                            i_2 = i
                    if i_2 > i_1:
                        answer = score.copy()
            return

        if cnt > info[l]:
            score[l] = info[l] + 1
            dfs(l+1, cnt-(info[l] + 1))
            score[l] = 0

        dfs(l+1, cnt)

    dfs(0, n)


    return answer