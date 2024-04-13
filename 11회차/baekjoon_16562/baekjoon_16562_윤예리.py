import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)

    # 친구비가 더 싼 쪽이 부모가 된다.
    if fee[x] < fee[y]:
        parents[y] = x
    else:
        parents[x] = y

n, m, k = map(int,input().split())
parents = [i for i in range(n+1)]
fee = [0] + list(map(int, input().split()))
for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)

# print(parents)
# 순회하면서 부모의 합쳐주기
f_set = set()
for i in range(1, n+1):
    f_set.add(find(i))
# print(f_set)

cost = 0
for j in f_set:
    cost += fee[j]
if cost <= k:
    print(cost)
else:
    print('Oh no')