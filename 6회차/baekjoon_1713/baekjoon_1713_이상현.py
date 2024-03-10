# 백준 1713번 후보 추천하기

from heapq import*

N = int(input())
input()
list_ = list(map(int, input().split()))
# 현재 사진틀에 있는 학생의 정보를 저장하는 딕셔너리
# 0번 인덱스는 그 학생이 추천받은 횟수
# 1번 인덱스는 그 학생이 사진틀에 게시되고 경과한 시간
# 2번 인덱스는 그 학생의 번호
temp_dict = {}

for num in list_:
    # 현재 사진틀에 있는 학생의 1번 인덱스값을 1 감소
    # 결과적으로, 사진틀에 게시되고 난 후 
    # 경과한 시간만큼 마이너스 방향으로 값이 커짐
    for i in temp_dict:
        temp_dict[i][1] -= 1

    if num in temp_dict:
        temp_dict[num][0] += 1
    else:
        if len(temp_dict) >= N:
            temp_list = list(temp_dict.values())
            heapify(temp_list)
            del temp_dict[heappop(temp_list)[2]]
            temp_dict[num] = [1, 0, num]
        else:
            temp_dict[num] = [1, 0, num]

print(*sorted(temp_dict.keys()))