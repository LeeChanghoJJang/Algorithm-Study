T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    m, n = map(int, input().split())
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))
    q = int(input())
    for i in range(q):
        Y = int(input())
        yi = (Y % m)-1
        yj = (Y % n)-1

        print(s[yi]+t[yj], end=' ')
    print()