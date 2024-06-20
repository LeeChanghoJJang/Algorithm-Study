# # A-F 0-5 // B-D 1-3// C-E 2-4//

import sys

t = int(input())

dices = [[] for _ in range(t)]

for i in range(t):
    num = list(map(int, sys.stdin.readline().strip().split()))

    dices[i].append([num[0],num[5]])            # 마주보는 면마다 따로따로 나눠 담기

    dices[i].append([num[1],num[3]])
    
    dices[i].append([num[2],num[4]])

output = 0
# 초기 설정값을 뭘로 두느냐 / target을 하나씩 옮겨가면서 검색 시작 
for dice in dices[0]:       
    for target in dice:                     
        total = 0
        # 검색 시작
        for idx in range(t):                
            for dice in dices[idx]:         # 1번을 포함한 각 주사위에서
                if target in dice:          # 마주보게 쌓을 면이 안에 있으면,

                    if 6 in dice:           # 근데 그 안에 6 이 있다?
                        if 5 in dice:       # 5도 같이 있다?
                            total += 4      # 그럼 4 쓰기
                        else:
                            total += 5      # 5 있으면 5
                    else:
                        total += 6          # 6 없으면 6 쓰기
                    # 다음 타겟 설정
                    if target == dice[0]:   # dice는 2개씩 묶여있는 형태이므로
                        target = dice[1]    # 만약 지금 타겟과 dice 값이 같으면 뒤집어줘야한다
                        break

                    else:
                        target = dice[0]    # 지금 타겟과 다르다(반대편 것을 썼다) 첫번째꺼 쓰면 된다.
                        break
        if total > output:                  # 최대값 비교
            output = total
print(output)                               # 출력