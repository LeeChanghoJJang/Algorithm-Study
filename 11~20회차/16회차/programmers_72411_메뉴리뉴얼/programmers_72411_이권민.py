# 각 코스 개수별로 order들에서 조합 생성, 가장 많이 나온 조합 구해서 append
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
#        빈도 출력.
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
#     빈도 순으로 정렬된 sorted_candidates에서 가장 많은 빈도수인 메뉴와 빈도가 같으 애들 append
    return sorted(answer)