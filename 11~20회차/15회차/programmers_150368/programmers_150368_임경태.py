# 이모티콘 할인행사 (2023 KAKAO BLIND RECRUITMENT)
from itertools import product

def solution(users, emoticons):
    ans = []

    # 가능한 할인율 조합 생성
    for rates in product((10, 20, 30, 40), repeat=len(emoticons)):
        cnt, price = 0, 0

        # 각 사용자에 대하여
        for user_rate, user_price in users:
            now_cnt, now_price = 0, 0

            # 각 이모티콘에 대하여
            for rate, emoticon in zip(rates, emoticons):

                # 현재 할인율이 사용자의 기대 할인율 이상인 경우
                if rate >= user_rate:
                    now_price += (emoticon // 100 * (100 - rate))

                # 현재 가격이 사용자의 기대 가격 이상이면
                if now_price >= user_price:
                    now_cnt += 1; break

            # 만약 현재 사용자가 만족했다면
            if now_cnt == 1:
                cnt += 1  # 전체 만족하는 사용자 수 증가
            else:
                price += now_price  # 만족하지 않으면 가격 추가

        ans.append([cnt, price])

    return sorted(ans, key=lambda x: (-x[0], -x[1]))[0]