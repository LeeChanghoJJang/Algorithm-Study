N, a, b = map(int, input().split())

if a + b > N + 1:
    exit(print(-1))

max_height = max(a, b)
s = a >= b

buildings = [i for i in range(1, max_height+1)]

c = b if s else a
c -= 1
left_buildings = [i for i in range(c, 0, -1)]
buildings += left_buildings
if not s:
    buildings.reverse()

rem = N - len(buildings)
if rem > 0:
    buildings = [buildings[0]] + [1] * rem + buildings[1:]
print(*buildings)