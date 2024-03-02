t = int(input())

for idx in range(t):
    size = int(input())
    farm = [input() for _ in range(size)]

    result = 0
    core = size//2
    w = 0
    for i in range(size):
        result += sum(map(int,farm[i][core-w : core+w+1]))
        if i < core:
            w += 1 
        elif i >= core :
            w -= 1
    print(f"#{idx+1} {result}")