# 캐시

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    cnt = 0
    for city in cities:
        city = city.lower()

        if city in cache :
            answer += 1
            cache.remove(city)
            cache.append(city)
            continue

        else :
            answer += 5
            
        if cacheSize != 0 :
            if cnt == cacheSize :
                cache.popleft()
                cache.append(city)
            else :
                cnt += 1
                cache.append(city)
        
    return answer