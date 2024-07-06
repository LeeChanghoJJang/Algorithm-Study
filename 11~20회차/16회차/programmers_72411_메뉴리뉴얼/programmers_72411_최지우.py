from itertools import combinations

def solution(orders, course):
    answer = []

    for length in course:
        cnt = {}

        for order in orders:
            for com in combinations(order, length):
                std_c = ''.join(sorted(com))

                if std_c in cnt:
                    cnt[std_c] += 1
                else:
                    cnt[std_c] = 1

        max_order = [k for k, v in cnt.items() if ((v == max(cnt.values())) and v >= 2)]
        answer.extend(max_order)
    answer.sort()

    return answer
