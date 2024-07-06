input()
chu = list(map(int, input().split()))
input()
goosle = list(map(int, input().split()))

dp = {0}

for i in chu:
    set_ = set()

    for j in dp:
        set_.add(j + i)
        set_.add(abs(j - i))

    dp |= set_

for w in goosle:
    if w in dp:
        print('Y', end=' ')
    else:
        print('N', end=' ')