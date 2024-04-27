# stack 사용
N = int(input())
a = 0

for n in range(N):
    stack = []
    top = -1
    result = []

    string = input()
    for s in string:
        if top == -1:
            stack.append(s)
            top += 1
        elif s == stack[top]:
            stack.pop()
            top -= 1
        else:
            stack.append(s)
            top += 1
    if len(stack) != 0:
        result.append(1)

    if sum(result) == 0:
        a += 1
print(a)