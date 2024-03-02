# 2116 주사위 쌓기
# 목표 : 한 옆면 숫자들 합의 최댓값 구하기
# 관건 : 처음 주사위에 의해 모든 다른 값 픽스
# 겹치는 면 제외한 다른 면에서 최댓값 추출

import sys
sys.stdin = open("input.txt")

dices = [tuple(map(int, input().split())) for _ in range(int(input()))]
opp = (5, 3, 4, 1, 2, 0)
max_v = 0

for i in range(1, 7):
    temp_max = 0
    top = i
    for dice in dices:
        bot = top
        top = dice[opp[dice.index(bot)]]
        temp_max += max(j for j in range(1, 7) if j != bot and j != top)

    max_v = max(max_v, temp_max)

print(max_v)
