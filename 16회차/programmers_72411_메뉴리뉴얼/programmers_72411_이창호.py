from itertools import combinations

def solution(orders, course):
    order_dict = {}
    max_len = {i: 0 for i in course}
    for length in course:
        for cook in orders:
            for a in combinations(cook, length):
                b = ''.join(sorted(a))
                if b not in order_dict:
                    order_dict[b] = 1
                else:
                    order_dict[b] += 1
                    lens = len(b)
                    if max_len[lens] < order_dict[b]:
                        max_len[lens] = order_dict[b]

    result = sorted(filter(lambda x: order_dict[x] >= 2, order_dict.keys()))

    total_result = []
    for i in result:
        if max_len[len(i)] == order_dict[i]:
            total_result.append(i)
    return total_result