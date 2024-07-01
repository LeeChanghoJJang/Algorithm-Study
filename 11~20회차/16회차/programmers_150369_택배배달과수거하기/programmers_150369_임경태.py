# 택배 배달과 수거하기 (2023 KAKAO BLIND RECRUITMENT)

def solution(cap, n, deliveries, pickups):
    answer = 0
    deli_item = 0
    pick_item = 0

    # 가장 먼 곳부터 탐색
    for i in range(n-1, -1, -1):
        # 현재 위치에서 배달과 수거할 물건의 수를 추가
        deli_item += deliveries[i]
        pick_item += pickups[i]

        # 배달 또는 수거할 물건이 남아있는 동안 반복
        while deli_item > 0 or pick_item > 0:
            # 각 위치의 배달과 수거 값에서 cap값 감산
            deli_item -= cap
            pick_item -= cap
            # 왕복 횟수 합산
            answer += (i+1)*2

    return answer