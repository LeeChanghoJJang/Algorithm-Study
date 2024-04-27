line = []

t = int(input())

numbers=list(map(int,input().split()))

for i in range(t):
    line.insert(i-numbers[i], i+1)
print(*line)