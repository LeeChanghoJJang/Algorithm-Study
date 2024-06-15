T = int(input())
# dp = [1] + [0] * 10**18

for _ in range(T):
    n = int(input())

    if n%10: print(0)
    else: print(1)