import sys
sys.stdin = open('input.txt')

def multi(x, y, a, b):    # x: 작은 값, y: 큰 값
    result = []
    for i in range(y-x+1):
        value = 0
        for j in range(x):
            value += a[j]*b[j+i]
        result.append(value)
    return max(result)

T = int(input())
for tc in range(1, 11):
    print(f'#{tc}', end=' ')
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m:
        print(multi(n, m, a, b))
    else:
        print(multi(m, n, b, a))


