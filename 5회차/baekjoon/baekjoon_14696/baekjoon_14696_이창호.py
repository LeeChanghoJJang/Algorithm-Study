# 별 4> 동그라미3 > 네모 2> 세모1
# a는 1~100 b는 1~100
import sys
sys.stdin = open('input.txt')
def game(A,B):
    while A and B:
        pattern1 = A.pop()
        pattern2 = B.pop()
        if pattern1 > pattern2:
            return 'A'
        elif pattern1 < pattern2:
            return 'B'

    else:
        if len(A) > len(B):
            return 'A'
        elif len(A) < len(B):
            return 'B'
        elif len(A) == len(B):
            return 'D'

N = int(input())
for i in range(N):
    num1,*A = map(int,input().split())
    num2,*B = map(int,input().split())
    A.sort()
    B.sort()
    print(game(A,B))