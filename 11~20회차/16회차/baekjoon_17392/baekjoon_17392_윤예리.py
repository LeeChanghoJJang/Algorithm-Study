import sys
input = sys.stdin.readline

# k만큼 행복하면 k+1일동안은 우울함의 합이 0

n, m = map(int, input().split())
happy = list(map(int, input().split()))
total = sum(happy)

if total >= m:
    exit(print(0))

mood = 0
idx = 0
for i in range(m):
    mood -= 1
    if mood < 0:
        if idx < n:
            mood = happy[idx]
            idx += 1
        else:
            cnt = i
            break

ans = 0
idx = 1
square = 1
while idx <= cnt:
    for i in range(n+1):
        if idx > cnt:
            break
        ans += square ** 2
        idx += 1
    square += 1

print(ans)