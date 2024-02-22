T = int(input())
for tc in range(1,T+1):
    years = []
    N,M = map(int,input().split())
    str_1 = input().split()
    str_2 = input().split()
    Q = int(input())
    for _ in range(Q):
        years.append(int(input()))
    print(f'#{tc}',end=' ')
    for i in years:
        print(str_1[i%N-1] +str_2[i%M-1],end=' ')
    print()