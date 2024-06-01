import sys
input = sys.stdin.readline

def check(sign, x, y):
    x = int(x); y = int(y)
    if sign == '>':
        if x > y:
            return True
    else:
        if x < y:
            return True
    return False

def dfs(value, d):
    if d == n+1:
        result.append(value)
        return

    for i in range(10):
        if not visited[i]:
            if d == 0 or check(ineq[d-1], value[d-1], str(i)):
                visited[i] = True
                dfs(value+str(i), d+1)
                visited[i] = False

n = int(input())
ineq = list(input().split())
visited = [False] * 10
result = []
dfs('', 0)
result.sort()
print(result[-1])
print(result[0])

