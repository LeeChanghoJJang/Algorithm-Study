# N+1 카드게임 (2024 KAKAO WINTER INTERNSHIP)

from heapq import heappush, heappop

def solution(coin, cards):
    N = len(cards)
    used = []
    Q = []

    # 첫 N/3 개 카드 사용
    for i in range(N//3):
        card = cards[i]
        used.append(card)

        # 현재 카드의 반대 카드도 사용되었는지 확인
        if N+1-card in used and cards.index(N+1-card) < N//3:
            heappush(Q, [0, card])

    round = 1
    i = N//3

    while i < N:
        # 2개 카드 사용
        for _ in range(2):
            card = cards[i]
            used.append(card)

            # 반대 카드가 이미 사용된 경우
            if N+1-card in used:
                # 반대 카드가 처음 N/3 구간에 있었는지 확인
                if cards.index(N+1-card) < N//3:
                    heappush(Q, [1, card])
                else:
                    heappush(Q, [2, card])
            i += 1

        if not Q: break

        # 최소 비용의 카드 사용
        c, _ = heappop(Q)

        if coin >= c: coin -= c
        else: break

        round += 1

    return round