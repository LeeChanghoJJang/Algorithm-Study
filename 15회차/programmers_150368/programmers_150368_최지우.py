# 이모티콘 할인행사 lv3
from itertools import product


def solution(users, emoticons):
    dc_rate = [10, 20, 30, 40]
    rates = list(product(dc_rate, repeat=len(emoticons)))

    result = []
    for rate in rates:
        cnt = 0
        total_price = 0

        for user in users:
            dc, price = user
            tmp = 0

            for i in range(len(emoticons)):
                if dc <= rate[i]:
                    tmp += int(emoticons[i] * (100-rate[i]) / 100)

            if tmp >= price:
                cnt += 1
            else:
                total_price += tmp

        result.append([cnt, total_price])

    answer = sorted(result, key=lambda x: (-x[0], -x[1]))[0]

    return answer

# users = [[40, 10000], [25, 10000]]
# emoticons = [7000, 9000]
# [1, 5400]

users = [
    [40, 2900], [23, 10000], [11, 5200],
    [5, 5900], [40, 3100], [27, 9200], [32, 6900]
]
emoticons = [1300, 1500, 1600, 4900]
# [4, 13860]
print(solution(users, emoticons))
