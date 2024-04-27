T = int(input())
 
for tc in range(T):
    N, M = map(int, input().split())
    list_ = [list(input()) for _ in range(N)]
    cnt_list = [[M - row.count(char_) for row in list_] for char_ in 'WBR']
    min_ = float('inf')
 
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            min_ = min(min_, sum(cnt_list[0][:i] + cnt_list[1][i:j] + cnt_list[2][j:]))
 
    print(f'#{tc + 1} {min_}')