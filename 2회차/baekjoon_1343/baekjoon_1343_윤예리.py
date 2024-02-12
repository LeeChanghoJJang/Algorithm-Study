board = input()
a = 'AAAA'
b = 'BB'
num_of_x = 0
answer = []

for i in board:
    if i == 'X':
        num_of_x += 1

    if num_of_x == 4:   # 4개 연속 X일 때 AAAA로 변환
        answer.append(a)
        num_of_x = 0

    if i == '.':        # .을 만났을 때
        if num_of_x == 2:       # 남은게 XX이면 BB로 변환
            answer.append(b)
            answer.append('.')
            num_of_x = 0
        elif num_of_x % 2 != 0: # -1
            answer = [-1]
            break
        else:                   # 그냥 . 반환
            answer.append('.')
            num_of_x = 0

if num_of_x == 2:
    answer.append(b)
elif num_of_x != 0:
    answer = [-1]

print(*answer, sep='')

