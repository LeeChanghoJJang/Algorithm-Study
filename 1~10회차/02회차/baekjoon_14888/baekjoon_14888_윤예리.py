n = int(input())
a = list(map(int, input().split()))
pls, mns, mul, div = map(int, input().split())

max_v = 1000000000
min_v = -1000000000

def dfs(idx, result, pls, mns, mul, div):
    global max_v, min_v

    if idx == n:
        max_v = max(max_v, result)
        min_v = min(min_v, result)
        return

    if pls > 0:
        dfs(idx + 1, result + a[idx], pls - 1, mns, mul, div)
    if mns > 0:
        dfs(idx + 1, result - a[idx], pls, mns - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, result * a[idx], pls, mns, mul - 1, div)
    if div > 0:
        next_result = int(result / a[idx]) if result >= 0 else -((-result) // a[idx])
        dfs(idx + 1, next_result, pls, mns, mul, div - 1)

dfs(1, a[0], pls, mns, mul, div)
print(max_v)
print(min_v)