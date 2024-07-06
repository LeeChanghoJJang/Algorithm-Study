from collections import deque
def solution(coin,cards):
    N = len(cards)
    init = cards[:N//3]
    cards = deque(cards[N//3:])
    temp = set()
    round = 1
    def pre_test(temp, init):
        for i in temp:
            for j in init:
                if i!=j and i+j == N+1:
                    temp.remove(i)
                    init.remove(j)
                    return True
        return False

    def merge(cards):
        if cards: temp.update({cards.popleft(),cards.popleft()})

    while cards:
        merge(cards)
        # 1단계 : 사전에 init에서 N+1이 발견된다면 다음 라운드로
        if pre_test(init,init):
            round += 1
        # 2단계 : 기존 init에 없고, 선택한 1개 중에 있다면 (코인 1개 감소)
        elif coin >=1 and pre_test(init,temp):
            coin-=1
            round += 1
        # 3단계 : 기존 init에 없고, 선택한 2개를 포함해 있다면 (코인 1개 감소)
        elif coin>=2 and pre_test(temp,temp):
            coin -=2
            round += 1
        else:
            break
    return round