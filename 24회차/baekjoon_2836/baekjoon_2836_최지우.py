import sys
input = sys.stdin.readline

N, M = map(int, input().split())

left = []

for _ in range(N):
    start, end = map(int, input().split())
    if start < end:
        pass
    else:
        left.append((end, start))

left.sort()
result = M
now_start, now_end = left[0]
rev = 0

for end, start in left[1:]:
    if end > now_end:
        rev += now_end - now_start
        now_start, now_end = end, start
    else:
        now_end = max(now_end, start)

rev += now_end - now_start
result += 2 * rev

print(result)