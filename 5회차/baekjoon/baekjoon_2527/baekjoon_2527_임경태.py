# 2527 직사각형

import sys
sys.stdin = open('input.txt')

for _ in range(4):
    s1_x, s1_y, e1_x, e1_y, s2_x, s2_y, e2_x, e2_y = map(int, input().split())
    max_x, max_y = max(s1_x, s2_x), max(s1_y, s2_y)
    min_x, min_y = min(e1_x, e2_x), min(e1_y, e2_y)

    if min_x < max_x or min_y < max_y:
        print('d')
    elif min_x == max_x and min_y == max_y:
        print('c')
    elif min_x == max_x or min_y == max_y:
        print('b')
    else:
        print('a')

'''
for _ in range(4):
    info = list(map(int, input().split()))
    info = sorted([info[:4], info[4:]])
    sq1_s, sq2_s = info[0][:2], info[1][:2]
    sq1_e, sq2_e = info[0][2:], info[1][2:]
    
    # x좌표에 따른 분기
    if sq1_e[0] < sq2_s[0]:
        print('d')
    elif sq1_e[0] == sq2_s[0]:
        #  y 좌표에 따른 분기
        if sq1_e[1] < sq2_s[1] or sq1_s[1] > sq2_e[1]:
            print('d')
        elif sq1_e[1] == sq2_s[1] or sq1_s[1] == sq2_e[1]:
            print('c')
        else:
            print('b')
    else:
        # y 좌표에 따른 분기
        if sq1_e[1] < sq2_s[1] or sq1_s[1] > sq2_e[1]:
            print('d')
        elif sq1_e[1] == sq2_s[1] or sq1_s[1] == sq2_e[1]:
            print('b')
        else:
            print('a')
'''