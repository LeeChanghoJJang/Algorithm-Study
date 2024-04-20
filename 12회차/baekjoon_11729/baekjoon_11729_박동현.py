def recur(height, start=1, end=3) :
    print(start,end)

    if height > 1 :
        recur(height-1, start , (1+2+3)-start-end)
        recur(height-1, (1+2+3)-start-end, end)


N = int(input())
ans = []

print(2**N-1)
recur(N)