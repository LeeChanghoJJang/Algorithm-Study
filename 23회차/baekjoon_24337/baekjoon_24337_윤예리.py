n, a, b = map(int, input().split())
answer = [i for i in range(1, a)] + [max(a, b)] + [i for i in range(b-1, 0, -1)]

if len(answer) > n: print(-1)
else:
    print(answer[0], end=' ')
    for i in range(n-len(answer)):
        print(1, end=' ')
    for i in range(1, len(answer)):
        print(answer[i], end=' ')