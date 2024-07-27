import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

n = int(input())
villages =[]
for _ in range(n):
    x,a = map(int,input().split())
    villages.append((x,a))

villages.sort()
total = sum(a for x,a in villages)
half = total / 2
current = 0
for x,a in villages:
    current +=a
    if current >= half:
        print(x)
        break