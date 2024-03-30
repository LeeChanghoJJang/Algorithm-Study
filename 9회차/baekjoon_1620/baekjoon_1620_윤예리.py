n, m = map(int, input().split())
poketmon = dict()
for i in range(1, n+1):
    j = input()
    poketmon[str(i)] = j
    poketmon[j] = str(i)

for j in range(m):
    find = input()
    print(poketmon[find])

'''
pypy 149288KB, 4796ms
'''