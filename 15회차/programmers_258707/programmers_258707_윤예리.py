from collections import deque

def check(deck1, deck2, target):
    deck2 = set(deck2)
    for card in deck1:
        if target - card in deck2:
            deck1.remove(card)
            deck2.remove(target-card)
            return True
    return False

def solution(coin, cards):
    in_hand = cards[:len(cards)//3]
    deck = deque(cards[len(cards)//3:])
    tmp = []
    t = 1

    while coin >= 0 and deck:
        tmp.append(deck.popleft())
        tmp.append(deck.popleft())

        # 손에 든 카드로만 턴 넘기기
        if check(in_hand, in_hand, len(cards)+1):
            pass
        # 손에 든 카드 1, 뽑은 카드 1
        elif coin >= 1 and check(in_hand, tmp, len(cards)+1):
            coin -= 1
        # 뽑은 카드 2
        elif coin >= 2 and check(tmp, tmp, len(cards)+1):
            coin -= 2
        else:
            break
        t += 1
    return t

print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
print(solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))