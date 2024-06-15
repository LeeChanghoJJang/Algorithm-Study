N = int(input())
w = list(map(int, input().split()))
w.sort()

t = 1
for i in w:
    if t < i:
        break
    t += i

print(t)