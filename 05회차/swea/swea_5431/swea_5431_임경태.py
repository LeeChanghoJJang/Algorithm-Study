import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, K = map(int, input().split())
    submit = tuple(map(int, input().split()))
    unsubmit = [i for i in range(1, N+1) if i not in submit]
    print(f'#{tc+1}', *unsubmit)
