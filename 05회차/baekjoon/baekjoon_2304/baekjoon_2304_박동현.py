# 내 양 옆의 것이 나보다 작으면 채택
# 최대치를 채택해서 양옆으로 계산
# 양 끝을 기준으로 시작해서, 채택된 값보다 작다면 그냥 채택된 값으로 바꿔서 합산

t = int(input())
ware_house = [0] * 1001     # L은 1000 이하다.
for _ in range(t) :
    L,H = map(int,input().split())
    ware_house[L] = H

max_value = max(ware_house) # 최대치

rem = 0     # 채택된 값

for idx in range(1001):
    if ware_house[idx] == max_value:
        rem = 0
        break
    if ware_house[idx] > rem:   # 창고에 저장된 값이 rem보다 높으면
        rem = ware_house[idx]   # 렘을 idx로 설정
    else:
        ware_house[idx] = rem   # 창고템을 rem 길이로 덮기

for i in range(1000,idx-1,-1):
    if ware_house[i] > rem:
        rem = ware_house[i]
    else :
        ware_house[i] = rem

print(sum(ware_house))