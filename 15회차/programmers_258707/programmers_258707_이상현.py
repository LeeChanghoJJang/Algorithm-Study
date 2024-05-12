from collections import deque

def has_pair(deck1, deck2, target):
    set_ = set(deck2)

    for card in deck1:
        if target - card in set_:
            deck1.remove(card)
            deck2.remove(target-card)
            return True
    return False


def solution(coin, cards):
    hand_size = len(cards) // 3
    hand = cards[:hand_size]
    deck = deque(cards[hand_size:])
    len_ = len(cards)
    pending = []
    answer = 1

    while coin >= 0 and deck:
        pending.append(deck.popleft())
        pending.append(deck.popleft())

        if has_pair(hand, hand, len_+ 1):
            pass
        elif coin >= 1 and has_pair(hand, pending, len_ + 1):
            coin -= 1
        elif coin >= 2 and has_pair(pending, pending, len_ + 1):
            coin -= 2
        else:
            break
        answer += 1

    return answer
