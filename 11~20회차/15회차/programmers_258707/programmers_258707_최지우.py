# n + 1 카드게임 lv3

def solution(coin, cards):
    n = len(cards)

    start_card = cards[:n//3]
    op_pair = {i: n+1-i for i in range(1, n+1)}

    get_cards = []

    idx = n//3
    turn = 0
    while idx <= n:
        turn += 1
        if idx == n:
            break
        c1, c2 = cards[idx:idx+2]

        if coin and op_pair[c1] in start_card:
            coin -= 1
            start_card.append(c1)
        else:
            get_cards.append(c1)

        if coin and op_pair[c2] in start_card:
            coin -= 1
            start_card.append(c2)
        else:
            get_cards.append(c2)

        for i in range(len(start_card)):
            tmp = start_card[i]
            if op_pair[tmp] in start_card:
                start_card.remove(tmp)
                start_card.remove(op_pair[tmp])
                idx += 2
                break
        else:
            for i in range(len(start_card)):
                tmp = start_card[i]
                if op_pair[tmp] in get_cards:
                    if coin:
                        coin -= 1
                        start_card.remove(tmp)
                        get_cards.remove(op_pair[tmp])
                        idx += 2
                        break
            else:
                if coin >= 2:
                    for i in range(len(get_cards)):
                        tmp = get_cards[i]
                        if op_pair[tmp] in get_cards:
                            get_cards.remove(tmp)
                            get_cards.remove(op_pair[tmp])
                            coin -= 2
                            idx += 2
                            break
                    else:
                        break
                else:
                    break
    answer = turn

    return answer


coin = 10
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(solution(coin, cards))

'''
1 ~ n 까지 카드 있음 ( n = 6 * k )
n // 3 개 카드 들고 시작

2장을 뽑고, 카드 하나 당 코인 하나를 쓰고 들고가기 / 버리기 선택
n + 1이 되면 카드 두 장을 내면 다음 라운드 갈 수 있음

n + 1이 되는 쌍이 n//2개 생김 => 짝 정해져 있음

당장 낼 수 있는 카드 뽑으면 코인 무조건 쓴다 생각하고,
    보관 후 내는거 까지가 한 턴 <=== 낼 수 있는 카드 뽑아도 코인은 써야 함

그냥 받는 카드 다 모아놓고, 다음 라운드로 넘길 수 있을 때 코인을 내는 느낌으로
'''