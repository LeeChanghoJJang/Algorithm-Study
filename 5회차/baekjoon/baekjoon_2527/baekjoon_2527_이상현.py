def chk(x1, y1, p1, q1, x2, y2, p2, q2):
    if x2 > p1 or x1 > p2 or y2 > q1 or y1 > q2:
        return 'd'

    if p1 == x2 or x1 == p2:
        if q1 == y2 or y1 == q2:
            return 'c'
        return 'b'

    if q1 == y2 or y1 == q2:
        return 'b'
    return 'a'

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    print(chk(x1, y1, p1, q1, x2, y2, p2, q2))