import sys
input = sys.stdin.readline

def isPrime(num):
    for i in range(2, int(num ** (0.5)) + 1):
        if num % i == 0:
            return False
    return True

def dfs(num):
    global N

    if not isPrime(num):
        return

    if len(str(num)) == N:
        print(num)
        return

    for i in range(1, 10):
        if i & 1:
            dfs(num * 10 + i)

N = int(input())
dfs(2)
dfs(3)
dfs(5)
dfs(7)