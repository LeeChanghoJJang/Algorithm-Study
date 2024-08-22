def dfs(idx=0):
    tmp = []
    for i in tree[idx]:
        dfs(i)
        tmp.append(DP[i])
    if tmp:                     # 그리디: 직속부하가 많은 사람부터
        tmp.sort(reverse=True)
        time = [tmp[i]+i+1 for i in range(len(tmp))]
        DP[idx] = max(time)


N = int(input())
arr = [*map(int, input().split())]

tree = [[] for _ in range(N)]
for i in range(1, N):
    tree[arr[i]].append(i)

DP = [0]*N
dfs()

print(DP[0])
