# import sys

# input = sys.stdin.readline

# N,M,B = map(int,input().split())

# ground = []
# for _ in range(N):
#     ground.extend(list(map(int,input().split())))

# ans = float('inf')

# for i in range(min(ground),max(ground)+1):
#     tmp = list(map(lambda x : x-i, ground))
    
#     plus_tmp, minus_tmp = 0,0

#     for v in tmp :
#         if v < 0 :
#             minus_tmp-=v
#         else :
#             plus_tmp+=v

#     if sum(tmp) >= 0 or B >= minus_tmp - plus_tmp :
#         tmp = 2*plus_tmp + minus_tmp
        
#         if ans > tmp :
#             ans = tmp
#             height = i
        
#         else :
#             exit(print(ans, height))
#     else :
#         exit(print(ans, height))

# print(ans,height)
#### 시간초과 코드

import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

ground = []
for _ in range(N):
    ground.extend(list(map(int, input().split())))

min_time = float('inf')

for i in range(min(ground), max(ground) + 1):       # ground의 최소치부터 최대치까지 순회하면서
    need,dig = 0,0                                  # need : 메꾸는데 필요한 블럭 수 / dig : 파낸 블럭 수 

    for h in ground:
        if h < i :                                  # 한 지역의 높이가 순회하는 특정 높이보다 낮으면
            need += i - h                           # 블럭으로 채워넣어야함 (need ++)
        else:                                       # 특정 높이보다 높으면
            dig += h - i                            # 파내야함 (dig ++)
    
    if dig + B >= need:                             # 파내야하는 양 + 보유한 블럭이 채워넣어야하는 블럭보다 많아야함
        time = need + dig *2                        # 시간 계산

        if time <= min_time:                        # 최소 시간 계산
            min_time = time
            height = i

print(min_time, height)
