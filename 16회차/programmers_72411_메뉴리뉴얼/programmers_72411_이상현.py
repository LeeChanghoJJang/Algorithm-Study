from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        dict_ = {}

        for order in orders:
            combination = combinations(sorted(order), c)

            for comb in combination:
                key_ = ''.join(comb)

                if key_ in dict_:
                    dict_[key_] += 1
                else:
                    dict_[key_] = 1

        max_ = max(dict_.values(), default=0)

        for menu, cnt in dict_.items():
            if cnt == max_ and cnt > 1:
                answer.append(menu)

    return sorted(answer)