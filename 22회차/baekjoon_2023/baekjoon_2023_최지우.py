N = int(input())


def dfs(num, idx):
    if idx == N:
        if isPrime(num):
            print(num)
        return
    
    for i in range(1, 10, 2):
        if isPrime(num * 10 + i):
            dfs(num*10+i, idx+1)
    

def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if not num%i:
            return False
    return True


dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)