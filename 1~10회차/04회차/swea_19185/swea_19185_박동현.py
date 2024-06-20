# import sys
# sys.stdin = open("19185.txt")

t = int(input())
for idx in range(t):
    n,m = map(int,input().split())
    N = input().split()
    M = input().split()

    Q = int(input())
    result = []
    for _ in range(Q):
        year = int(input())

        result.append(f"{N[year%n-1]}{M[year%m-1]}")
    
    print(f"#{idx+1}", *result)