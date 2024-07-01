import sys
sys.stdin = open('input.txt')

n = int(input())
sol = sorted(map(int,input().split()))
result =[3*int(1e9)] + [int(1e9)] * 3

for k in range(n):
    i = k+1; j = n-1
    while i < j:
        total = sol[i] + sol[j] + sol[k]
        if abs(total) < result[0]: result = [abs(total),sol[k],sol[i],sol[j]]
        if total < 0:i += 1
        elif total > 0:j -= 1
        else: break
print(*result[1:])