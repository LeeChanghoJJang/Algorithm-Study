import sys
input = sys.stdin.readline

N = int(input())
list_ = sorted(list(map(int, input().split())) for _ in range(N))
s, e = list_[0]

result = 0

for i in range(1, N):
    ns, ne = list_[i]

    if ns >= e:
        result += e - s
        s, e = ns, ne

    else:
        e = max(e, ne)

result += e - s
print(result)