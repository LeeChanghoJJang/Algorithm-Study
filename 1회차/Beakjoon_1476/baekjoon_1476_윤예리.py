# E는 15까지, S는 28까지, M은 19까지
E, S, M = map(int, input().split())

i = max([E, S, M])
while i > 0:
    if (i - E) % 15 == 0 and (i - S) % 28 == 0 and (i - M) % 19 == 0:
        print(i)
        break
    else:
        i += 1
