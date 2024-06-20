import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    score = list(map(int,input().split()))
    result = []
    while K > 0:
        temp = max(score)
        score.remove(temp)
        result.append(temp)
        K-=1
    print(f'#{tc} {sum(result)}')