import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    parent = [0] * (n+1)

    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a

    x, y = map(int, input().split())
    parX, parY = [0, x], [0, y]

    while parent[x]:
        parX.append(parent[x])
        x = parent[x]

    while parent[y]:
        parY.append(parent[y])
        y = parent[y]

    i = 1
    while parX[-i] == parY[-i]: i += 1
    print(parX[-i+1])