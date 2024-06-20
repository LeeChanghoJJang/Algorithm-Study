a = int(input())        # 컴퓨터 수
b = int(input())        # 테스트 케이스 수
temp_list = []
for i in range(b):
    temp_set = set(map(int, input().split()))       # set로 받고 list에 저장
    temp_list.append(temp_set)

for j in range(b):                 
    for k in range(b):
        if temp_list[j] & temp_list[k]:             # 교집합이 있는 경우
            temp_list[j].update(temp_list[k])       # update해 한 단위로 병합

output = 0
for k in temp_list:         # 병합된 리스트의 각 원소에 대해
    if 1 in k:              # 1이 k에 들어있으면
        rem = len(k)        # 그 길이를 재서 비교
        if rem > output:
            output = rem

if output == 0:         # 없으면 0인데, 있는 경우 숙주를 제외하고 -1한 값을 출력
    print(0)
else:
    print(output-1)
