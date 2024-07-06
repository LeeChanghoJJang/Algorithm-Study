from itertools import product

def solution(users, emoticons):
    answer = (-1, -1)
    case_list = product([10, 20, 30, 40], repeat=len(emoticons))

    for case in case_list:
        cnt = 0
        sales_amount = 0

        for user in users:
            price = 0

            for discount_rate, emoticon_price in zip(case, emoticons):
                if user[0] > discount_rate:
                    continue
                price += emoticon_price * (1 - discount_rate / 100)

            if price >= user[1]:
                cnt += 1
            else:
                sales_amount += price

        if answer[0] < cnt or (answer[0] == cnt and answer[1] < sales_amount):
            answer = (cnt, sales_amount)
    return answer
