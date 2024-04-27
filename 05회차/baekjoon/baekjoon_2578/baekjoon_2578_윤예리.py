import sys
sys.stdin = open('input.txt')

def check_bingo():
    cnt = 0
    # 가로 확인
    for r in range(5):
        if sum(chulsu[r]) == 0:
            cnt += 1

    # 세로 확인
    for c in range(5):
        check = 0
        for r in range(5):
            check += chulsu[r][c]
        if check == 0:
            cnt += 1

    # 대각선 확인
    check_left = 0
    check_right = 0
    for r in range(5):
        check_left += chulsu[r][r]
        check_right += chulsu[4-r][r]
    if check_left == 0:
        cnt += 1
    if check_right == 0:
        cnt += 1

    if cnt >= 3:
        return True

chulsu = [list(map(int, input().split())) for _ in range(5)]
answer = [list(map(int, input().split())) for _ in range(5)]

b = False
for i in range(5):
    for j in range(5):
        num = answer[i][j]

        # 사회자가 부르는 수 삭제
        for k in range(5):
            if num in chulsu[k]:
                chulsu[k][chulsu[k].index(num)] = 0
                break

        # 삭제 후 확인
        if check_bingo():
            print(i*5+j+1)
            b = True
            break
    if b:
        break
