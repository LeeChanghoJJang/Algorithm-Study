from itertools import combinations
def solution(friends, gifts):
    # gift_index : 선물지수
    gift_index = {i: 0 for i in friends}
    # gift_relation : 각 친구가 각 선물한 친구를 딕셔너리로 구현
    gift_relation = {i: {j:0 for j in friends} for i in friends}
    # 선물한사람, 받은사람, 그 관계를 각각 저장
    for person in gifts:
        gifting, gifted = person.split(' ')
        gift_index[gifting] +=1
        gift_index[gifted] -=1
        gift_relation[gifting][gifted] +=1
    # will : 친구별로 앞으로 선물 받을 수를 저장함
    will = {i:0 for i in friends}
    # 모든 친구 중 두명씩을 중복없이 뽑아, 서로 선물 기록을 비교
    for person1,person2 in combinations(friends,2):
        if gift_relation[person1][person2] > gift_relation[person2][person1]:
            will[person1] +=1
        elif gift_relation[person1][person2] < gift_relation[person2][person1]:
            will[person2] +=1
        else:
            # 만약 기록이 없거나 같다면 선물지수에 따라 판정
            if gift_index[person1] < gift_index[person2]:
                will[person2] +=1
            elif gift_index[person2] < gift_index[person1]:
                will[person1] +=1
    return max(will.values())