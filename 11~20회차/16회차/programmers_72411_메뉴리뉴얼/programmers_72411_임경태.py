# 메뉴 리뉴얼 (2021 KAKAO BLIND RECRUITMENT)
from itertools import combinations

def solution(orders, course):
    answer = []
    menu_dict = {}
    length_dict = {}

    # 모든 주문에 대해 처리
    for order in orders:
        # 주문 내 가능한 모든 조합 생성
        for num in range(2, len(order)+1):
            for menu in combinations(order, num):
                word = ''.join(sorted(menu))
                if word in menu_dict:
                    menu_dict[word] += 1
                else:
                    menu_dict[word] = 1

    # 조합을 등장 빈도순으로 정렬
    for menu_freq in sorted(menu_dict.items(), key=lambda x: -x[1]):
        # 등장 빈도가 2 미만이면 패스
        if menu_freq[1] < 2:
            continue

        length = len(menu_freq[0])

        # 현재 조합의 길이가 course에 없으면 건너뜀
        if length not in course:
            continue

        # 해당 길이가 length_dict에 이미 있으면
        if length in length_dict:
            # 최대 빈도수와 같으면 answer에 추가
            if length_dict[length] == menu_freq[1]:
                answer.append(menu_freq[0])
        # 없으면
        else:
            # 해당 길이의 최대 빈도수를 length_dict에 저장하고 answer에 추가
            length_dict[length] = menu_freq[1]
            answer.append(menu_freq[0])

    # 결과를 사전순으로 정렬
    return sorted(answer)
