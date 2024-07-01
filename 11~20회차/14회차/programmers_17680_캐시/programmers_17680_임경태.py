# [1차] 캐시 (2018 KAKAO BLIND RECRUITMENT)
from collections import deque

def solution(S, cities):
    cacheQ = deque([], S)
    time = 0

    for city in cities:
        # 대문자로 통일
        city = city.upper()
        # 캐시에 도시가 있다면 +1
        if city in cacheQ:
            time += 1
            cacheQ.remove(city)
            cacheQ.append(city)
        # 캐시에 도시가 없다면 +5
        else:
            time += 5
            cacheQ.append(city)

    return time