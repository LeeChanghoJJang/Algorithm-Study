import sys
sys.stdin = open('input.txt')

def clockwise(i, j, x, y):
    result = 0

    while x != i or y != j:
        if x == 0 and y < m:        # 북
            y += 1
            result += 1

        elif y == m and x < n:      # 동
            x += 1
            result += 1

        elif x == n and y > 0:      # 남
            y -= 1
            result += 1

        else:                       # 서
            x -= 1
            result += 1

    else:
        return result


m, n = map(int, input().split())    # 블록의 가로(m), 세로 길이(n)
                                    # [10, 5]
k = int(input())    # 상점의 개수
store = []
for s in range(1, k+2):
    # 1: 북, 2: 남, 3: 서, 4: 동
    # 북, 남: 왼쪽으로부터의 거리
    # 동, 서: 위쪽으로부터의 거리
    direction, distance = map(int, input().split())
    if direction == 1:
        store.append((0, distance))
    elif direction == 2:
        store.append((n, distance))
    elif direction == 3:
        store.append((distance, 0))
    else:
        store.append((distance, m))

total = 0
# print(store)
length = (m+n)*2
dg = store.pop()

for s in store:
    dist = clockwise(s[0], s[1], dg[0], dg[1])
    total += min(dist, length - dist)
print(total)
