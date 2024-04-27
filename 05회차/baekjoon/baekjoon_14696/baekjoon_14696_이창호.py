# 별 4> 동그라미3 > 네모 2> 세모1
# a는 1~100 b는 1~100
import sys
sys.stdin = open('input.txt')
# A와 B를 매칭시켰을 때 승부여부를 가르는 함수
def game(A,B):
    # A와 B의 원소가 있을 때까지만
    while A and B:
        # 각각 하나씩 받음
        pattern1 = A.pop()
        pattern2 = B.pop()
        # 숫자가 크면 이기는 것
        if pattern1 > pattern2:
            return 'A'
        elif pattern1 < pattern2:
            return 'B'

    else:
        # 만약 위에서 결판이 안나고 길이가 다르다면
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
