import sys
sys.stdin = open('input.txt')
# 현재 시점에서 상대가 지는 경우가 하나라도 있다면 그 경우를 위해 최선을 다할것
# 만약 어떠한 경우라도 상대가 이기는 경우가 나오면 그 시점에서 패배

T = int(input())

while (T > 0):
    N = int(input())

    if N % 10 == 0:
        print('1')
    else:
        print('0')

    T -= 1

