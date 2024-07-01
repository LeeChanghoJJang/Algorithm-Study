
def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        city = city.lower()  # 대소문자 구분 없음
        if city in cache:  # cache hit
            answer += 1
            cache.remove(city)  # LRU 알고리즘을 위해 해당 도시를 제거하고
            cache.append(city)  # 리스트의 맨 뒤에 다시 추가하여 최근 사용으로 갱신
        else:  # cache miss
            answer += 5
            if cacheSize > 0:  # 캐시 크기가 0보다 큰 경우에만 캐시에 도시 추가
                if len(cache) >= cacheSize:  # 캐시가 가득 찬 경우 가장 오래된 도시 제거
                    cache.pop(0)
                cache.append(city)
    return answer
