import sys
sys.stdin =open('input.txt')
N = int(input())

def search(num,N):
    temp = [N,num]
    while N:
        if N-num < 0:
           break
        temp.append(N - num)
        N, num = num, N-num
    return temp

max_val = 0
result = []
for i in range(N+1):
    if max_val < len(search(i,N)):
        max_val = len(search(i,N))
        result = search(i,N)
print(max_val)
print(*result)

