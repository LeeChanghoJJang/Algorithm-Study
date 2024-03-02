import sys
sys.stdin = open('input.txt')

def comp(a1, a2, m, n):
    max_sum = 0
    for i in range(m-n+1):
        temp = 0
        for j in range(n):
            temp += a1[j] * a2[i+j]
        max_sum = max(max_sum, temp)
    return max_sum


for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        print(f'#{tc+1}', comp(A, B, M, N))
    else:
        print(f'#{tc+1}', comp(B, A, N, M))
