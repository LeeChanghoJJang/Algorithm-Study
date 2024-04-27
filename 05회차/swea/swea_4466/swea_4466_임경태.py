import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, K = map(int, input().split())
    score = sorted(list(map(int, input().split())), reverse=True)
    print(f'#{tc+1}', sum(score[:K]))