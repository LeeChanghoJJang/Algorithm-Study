def dfs(list_, d):
    for x in sorted(list_.keys()):
        print(' ' * d + x)
        dfs(list_[x], d + 1)

N = int(input())
child = {}

for _ in range(N):
    list_ = input().strip().split('\\')
    temp = child

    for x in list_:
        if x not in temp:
            temp[x] = {}
        temp = temp[x]

dfs(child, 0)