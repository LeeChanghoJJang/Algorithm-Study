def solution(friends, gifts):
    gift_dict = {}
    gift_cnt = {}
    for f in friends:
        gift_dict[f] = {}
        gift_cnt[f] = 0

    for gift in gifts:
        gift = list(gift.split())
        gift_cnt[gift[0]] += 1
        gift_cnt[gift[1]] -= 1

        if gift[1] in gift_dict[gift[0]]:
            gift_dict[gift[0]][gift[1]] += 1
        else:
            gift_dict[gift[0]][gift[1]] = 1

    get_gift = [0] * len(friends)
    for i in range(len(friends)):
        give = friends[i]
        for j in range(i+1, len(friends)):
            get = friends[j]

            # i가 준 선물 개수
            a = gift_dict[give][get] if get in gift_dict[give] else 0
            # j가 준 선물 개수
            b = gift_dict[get][give] if give in gift_dict[get] else 0

            if a > b:
                get_gift[i] += 1
            elif a < b:
                get_gift[j] += 1
            else:
                if gift_cnt[give] > gift_cnt[get]:
                    get_gift[i] += 1
                elif gift_cnt[give] < gift_cnt[get]:
                    get_gift[j] += 1


    answer = max(get_gift)
    return answer

print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))