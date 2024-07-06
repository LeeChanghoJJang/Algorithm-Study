N = int(input())
weight = list(map(int, input().split()))
M = int(input())
marble = list(map(int, input().split()))

max_ = sum(weight)

s = {0}
for w in weight:
    tmp = set()
    for i in s:
        tmp.add(i+w)
        tmp.add(abs(i-w))
    s = s | tmp

result = []

for m in marble:
    if m in s:
        result.append('Y')
    else:
        result.append('N')

print(*result)