def solution(friends, gifts):
    answer = 0

    gift_map = {}
    giver_map = {}
    receiver_map = {}
    answer_map = {}

    # map에 friends를 등록함.
    for f1 in friends:
        inner_gift_map = {}
        for f2 in friends:
            if f1 == f2:
                continue
            inner_gift_map[f2] = 0
        gift_map[f1] = inner_gift_map
        answer_map[f1] = 0
        giver_map[f1] = 0
        receiver_map[f1] = 0

    # 선물에 대한 데이터를 Map에 저장함.
    for gift in gifts:
        giver, receiver = gift.split()
        gift_map[giver][receiver] += 1
        giver_map[giver] += 1
        receiver_map[receiver] += 1

    # 두 사람에 대한 조합을 지정해야 함.
    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            A = friends[i]
            B = friends[j]

            A_count = gift_map[A][B]
            B_count = gift_map[B][A]

            if A_count > B_count:
                answer_map[A] += 1
            elif B_count > A_count:
                answer_map[B] += 1
            else:
                A_value = giver_map[A] - receiver_map[A]
                B_value = giver_map[B] - receiver_map[B]

                if A_value > B_value:
                    answer_map[A] += 1
                elif B_value > A_value:
                    answer_map[B] += 1

    return max(answer_map.values())