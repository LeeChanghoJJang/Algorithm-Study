# 양궁대회
from itertools import product

def solution(n, info):
    info.reverse()
    max_diff = 0
    ans = [-1]

    # 모든 가능한 선택 조합을 반복
    for win_comb in product((1, 0), repeat=11):
        arrows = sum(info[i] + 1 for i in range(11) if win_comb[i])

        # 선택 조합의 화살 수가 조건을 만족한다면
        if arrows <= n:
            A = sum(i for i in range(11) if not win_comb[i] and info[i])
            R = sum(i for i in range(11) if win_comb[i])
            score_diff = R - A

            # 최대 점수 차이 갱신
            if max_diff < score_diff:
                max_diff = score_diff
                ans = [n - arrows] + [info[i] + 1 if win_comb[i] else 0 for i in range(1, 11)]

    return ans[::-1]