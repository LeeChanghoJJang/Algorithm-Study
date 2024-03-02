w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

width = (p + t) // w
height = (q + t) // h

x = (p + t) % w if width % 2 == 0 else w - (p + t) % w
y = (q + t) % h if height % 2 == 0 else h - (q + t) % h

print(x, y)