import sys
sys.stdin = open('input.txt')
# 세분화 필요
def finds_distances(store_way,store_distance):
    result = 0
    if dongun_way != store_way:
        if dongun_way + store_way ==3: # 1 2 / 2 1 (북과 남)
            result += height
            result += min(dongun_distance + store_distance, 2*width - dongun_distance - store_distance)
        elif dongun_way + store_way ==4:
            result += dongun_distance + store_distance
        elif dongun_way + store_way == 5:
            if dongun_way == 1: # store_way = 4
                result += width - dongun_distance + store_distance
            elif dongun_way == 2: # store_way = 3
                result += height + dongun_distance - store_distance
            elif dongun_way == 3: # store_way = 2
                result += height - dongun_distance + store_distance
            elif dongun_way == 4: # store_way = 1
                result += dongun_distance + width - store_distance
        elif dongun_way + store_way == 6:
            result += width + height - dongun_distance - store_distance
        elif dongun_way + store_way == 7: # 3 4 / 4 3(서와 동)
            result += width
            result += min(2*height - dongun_distance - store_distance, dongun_distance + store_distance)
    else: # 아예 같은 경우 1 1 2 2 3 3 4 4
        result += abs(dongun_distance - store_distance)
    return result

width,height = map(int,input().split())
store = int(input())
distances = [list(map(int,input().split())) for _ in range(store)]
dongun_way, dongun_distance = map(int,input().split())
min_sum = 0

for i,j in distances:
    min_sum += finds_distances(i,j)
print(min_sum)