# 2629 양팔저울
_, weight_N = int(input()), list(map(int, input().split()))
_, weight_M = int(input()), list(map(int, input().split()))

DP = {0}

for w in weight_N:
    tmp = set()
    for i in DP:
        tmp.add(i + w)
        tmp.add(abs(i - w))
    DP |= tmp

print(*['Y' if w in DP else 'N' for w in weight_M])