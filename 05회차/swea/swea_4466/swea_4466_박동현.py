t = int(input())

for i in range(t):
    N,K = map(int,input().split())
    score = list(map(int,input().split()))
    score.sort(reverse=True)
    print(sum(score[:K]))
