from collections import deque
def solution(cacheSize, cities):
    result = []
    time= 0
    # 도시를 순회
    for city in cities:
        # 대문자 소문자 구분 없어 한가지로 통일
        city = city.lower()
        # 기존에 city가 없으면 city를 추가
        if city not in result:
            result.append(city)
            # 다만.. 캐시사이즈가 초과한다면 맨 첨에 들어간거는 빼고
            if len(result) > cacheSize:
                result.pop(0)
            # 새거가 들어가면 무조건 5초 증가
            time+=5
        # 기존에 city가 있다면?
        else:
            # 기존꺼를 갱신하기 위해 제거하고, 새거 추가
            result.remove(city)
            result.append(city)
            # 기존것이 있으면 1초 추가
            time+=1
    return time
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize,cities))