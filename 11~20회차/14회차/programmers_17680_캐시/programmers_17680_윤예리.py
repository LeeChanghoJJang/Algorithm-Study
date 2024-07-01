from collections import deque

def solution(cacheSize, cities):
    cache = deque([])
    answer = 0

    for city in cities:
        if cacheSize:
            if city not in cache:
                if len(cache) == cacheSize:
                    cache.popleft()
                cache.append(city)
                answer += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
        else:
            answer += 5
    return answer