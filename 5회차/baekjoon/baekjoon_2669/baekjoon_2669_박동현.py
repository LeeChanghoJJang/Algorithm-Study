square_list = [] # 각 좌표가 들어갈 이차원 리스트
max_value = 0 # 최대치 받아서 정방형 빈 리스트 만들 예정
for _ in range(4) :
    items = list(map(int,input().split())) # 리스트 만들고
    square_list.append(items) # 좌표 리스트에 담고
    if max(items) > max_value : # max 비교 같이하기
        max_value = max(items)
# 정방형 빈 리스트를 max_value 기반으로 할당
dimension = [[0 for _ in range(max_value)] for _ in range(max_value)]

# 색칠하기
for item in square_list :
    for idx_y in range(item[1],item[3]) :
        for idx_x in range(item[0],item[2]) :
            dimension[idx_y][idx_x] = 1

# 1의 개수 세기
space = 0
for i in dimension :
    space += i.count(1)
print(space)