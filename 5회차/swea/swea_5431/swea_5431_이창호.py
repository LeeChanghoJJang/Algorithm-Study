T = int(input())

for tc in range(1, T + 1):

    n, k = map(int, input().split())
    # print(n,k)
    peoples = list(map(int, input().split()))
    # print(peoples)

    nohomework = []
    for i in range(1, n + 1):
        if i not in peoples:
            nohomework.append(i)

    print(f'#{tc}', *nohomework)