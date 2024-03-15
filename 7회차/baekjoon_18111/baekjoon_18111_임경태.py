# 18111 마인크래프트 (실버2)

N, M, B = map(int, input().split())
arr = sorted(int(x) for _ in range(N) for x in input().split())
time = 1e+9; height = 0

for t in range(arr[-1], arr[0]-1, -1):
    temp = 0; block = B
    for n in arr:
        s = n - t
        if s < 0: temp -= s; block += s
        else: temp += 2*s; block += s
    if block >= 0 and time > temp:
        time = temp
        height = t

print(time, height)

'''
119764KB / 476ms
'''