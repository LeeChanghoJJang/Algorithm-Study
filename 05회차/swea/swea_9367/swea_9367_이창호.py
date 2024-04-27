import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    C = list(map(int,input().split()))
    max_val = 1
    cnt = 1
    for i in range(1,N):
        if C[i] > C[i-1]:
            cnt +=1
            max_val = cnt
        else:
            cnt=1
    print(f'#{tc} {max_val}')