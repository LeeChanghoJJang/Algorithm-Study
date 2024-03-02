import sys
sys.stdin = open('input.txt')

def winner(a, b):
    if a == b:
        return 'D'

    while a and b:
        ai = a.pop(0)
        bi = b.pop(0)
        if ai > bi:
            return 'A'
        elif ai < bi:
            return 'B'
        else:
            pass
    else:
        if a:
            return 'A'
        else:
            return 'B'

n = int(input())
for _ in range(n):
    # [별, 동그라미, 네모, 세모] = [4, 3, 2, 1]
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = sorted(A[1:], reverse=True)     # 정리된 리스트
    b = sorted(B[1:], reverse=True)
    print(winner(a, b))




