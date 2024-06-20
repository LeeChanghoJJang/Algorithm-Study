# 4259 제곱수의 합 계산하기
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    result =0

    for i in numbers:
        k,v = divmod(i,10)
        result+=k**v
    print(f'#{tc} {result}')


