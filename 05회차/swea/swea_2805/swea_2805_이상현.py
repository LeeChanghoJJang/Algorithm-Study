T = int(input())
 
for tc in range(T):
    N = int(input())
    list_ = [list(map(int, list(input()))) for _ in range(N)]
    sum_ = 0
 
    for row in range(N):
        for col in range(N):
            if abs(N // 2 - row) + abs(N // 2 - col) <= N // 2:
                sum_ += list_[row][col]
 
    print(f'#{tc + 1} {sum_}')