# 백준 1891번 사분면

d, numbers = map(int, input().split())
dx, dy = map(int, input().split())
result = ''
x, y = 0, 0

# 초기 좌표를 구하는 과정
for i, num in enumerate(str(numbers), start = 1):
    num = int(num)

    if num == 3:
        continue
    temp = 2 ** (d - i)

    if num == 1:
        x += temp
        y += temp
    elif num == 2:
        y += temp
    else:
        x += temp

x += dx
y += dy

for i in range(d):
    half = 2 ** (d - i - 1)

    if 0 <= x < half and 0 <= y < half:
        result += '3'

    elif 0 <= x < half and half <= y < 2 * half:
        y -= half
        result += '2'

    elif half <= x < 2 * half and 0 <= y < half:
        x -= half
        result += '4'

    elif half <= x < 2 * half and half <= y < 2 * half:
        x -= half
        y -= half
        result += '1'

[print(result if len(result) == d else -1)]