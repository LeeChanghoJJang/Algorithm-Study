# 가장 많이 받은 선물 (2024 KAKAO WINTER INTERNSHIP)

def solution(friends, gifts):
    giftLog = {friend: {} for friend in friends}  # 선물 로그
    giftIdx = {friend: 0 for friend in friends}  # 선물 지수

    # 주고받은 선물과 선물 지수 입력
    for gift in gifts:
        give, take = gift.split()

        if take in giftLog[give]:
            giftLog[give][take] += 1
        else:
            giftLog[give][take] = 1

        giftIdx[give] += 1
        giftIdx[take] -= 1

    # 누가 선물을 많이 받을지 예측
    will_get = [0 for _ in friends]
    for i in range(len(friends)):
        A = friends[i]

        for j in range(i+1, len(friends)):
            B = friends[j]
            # 선물을 주고 받은 기록 체크
            numA = giftLog[A][B] if B in giftLog[A] else 0
            numB = giftLog[B][A] if A in giftLog[B] else 0

            # 선물 지수 비교 및 카운트
            if numA > numB: will_get[i] += 1
            elif numA < numB: will_get[j] += 1
            else:
                ai, bi = giftIdx[A], giftIdx[B]
                if ai > bi: will_get[i] += 1
                elif ai < bi: will_get[j] += 1

    return max(will_get)