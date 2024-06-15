import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())

    if N % 10:
        print(0)
    else:
        print(1)