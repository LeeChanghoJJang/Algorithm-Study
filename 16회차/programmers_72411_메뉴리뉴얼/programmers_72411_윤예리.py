from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        cnt = {}

        for order in orders:
            comb = list(combinations(list(order), c))
            for co in comb:
                menu = ''.join(sorted(co))

                if menu in cnt:
                    cnt[menu] += 1
                else:
                    cnt[menu] = 1

        max_order = [k for k, v in cnt.items() if ((v == max(cnt.values())) and v >= 2)]
        answer.extend(max_order)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))