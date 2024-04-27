# 14888 연산자 끼워넣기
# DFS 구현 - 재귀 함수 활용 - 최댓값과 최솟값 갱신

import sys
sys.stdin = open("input.txt")

N = int(input())
operand = list(map(int, input().split()))  # 피연산자 배열
pls, mis, mlt, div = map(int, input().split())  # 각 연산자 개수
num_max = -10E+9; num_min = 10E+9

def DFS(i, num):
    global pls, mis, mlt, div, num_max, num_min
    if i == N:
        num_max = max(num_max, num)
        num_min = min(num_min, num)
    else:
        if pls > 0:
            pls -= 1
            DFS(i+1, num + operand[i])
            pls += 1
        if mis > 0:
            mis -= 1
            DFS(i+1, num - operand[i])
            mis += 1
        if mlt > 0:
            mlt -= 1
            DFS(i+1, num * operand[i])
            mlt += 1
        if div > 0:
            div -= 1
            if num < 0:
                DFS(i+1, -((-num) // operand[i]))
            else:
                DFS(i+1, num // operand[i])
            div += 1

DFS(1, operand[0])
print(f'{num_max}\n{num_min}')

'''
31120KB / 64ms
'''