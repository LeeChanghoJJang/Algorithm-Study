import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N%10:
        print(0)
    else:
        print(1)

'''
마지막 돌 가져오면 이김
한자리수 전부 팰린드롬
1 ~ 9 11 ~ 19
10 20
'''