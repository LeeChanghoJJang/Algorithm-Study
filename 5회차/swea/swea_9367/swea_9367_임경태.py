import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    C = list(map(int, input().split()))
    prev_carrot, cnt, ans = 0, 0, 0

    for carrot in C:
        if carrot > prev_carrot:
            cnt += 1
        else:
            if ans < cnt:
                ans = cnt
            cnt = 1
        prev_carrot = carrot

    if ans < cnt: ans = cnt
    print(f'#{tc+1} {ans}')
