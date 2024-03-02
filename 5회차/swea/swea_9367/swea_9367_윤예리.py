import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n = int(input())
    arr = list(map(int, input().split()))
    max_cnt = 1

    for i in range(n-1):            # arr 순회
        j = i
        cnt = 1
        while j < n-1:
            if arr[j] < arr[j+1]:   # 뒤 숫자가 더 크면
                cnt += 1            # cnt + 1
                j += 1
            else:
                break
        if max_cnt < cnt:           
            max_cnt = cnt

    print(max_cnt)
