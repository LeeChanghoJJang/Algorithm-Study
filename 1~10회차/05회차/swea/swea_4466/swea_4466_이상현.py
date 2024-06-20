T = int(input())
 
for tc in range(T):
    N, K = map(int, input().split())
    score_list = sorted(map(int, input().split()), reverse = True)
 
    print(f'#{tc + 1} {sum(score_list[i] for i in range(K))}')