import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    result = 0

    # 위 절반
    for i in range(n//2, -1, -1):
        for j in range(i, i+(n-2*i)):
            result += arr[n//2-i][j]

    # 아래 절반
    for i in range(1, n//2+1):
        for j in range(i, i+(n-2*i)):
            result += arr[n//2+i][j]

    print(result)