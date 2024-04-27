T = int(input())
 
for tc in range(T):
    N, _ = map(int, input().split())
    list_ = list(map(int, input().split()))
 
    print(f'#{tc + 1}', *[n for n in range(1, N + 1) if n not in list_])