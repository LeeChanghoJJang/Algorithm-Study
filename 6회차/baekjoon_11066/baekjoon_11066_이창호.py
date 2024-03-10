import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    k = int(input())
    f = list(map(int,input().split()))

    d = [[0] * k for _ in range(k)]
    # 첫번째는 각 행과 열을 더했을때 누적합을 D에 저장
    for i in range(k-1):
        d[i][i+1] = f[i] + f[i+1]
        for j in range(i+2, k):
            d[i][j] = d[i][j-1] + f[j]
    # 2칸이상 누적합부터
    for n in range(2,k):
        for i in range(k-n):
            j = i+n
            costs = [d[i][x] + d[x+1][j] for x in range(i,j)]
            d[i][j] += min(costs)

    print(d[0][k - 1])  # 모든 장을 합치는데 필요한 최소 비용