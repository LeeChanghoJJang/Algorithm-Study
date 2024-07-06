N, K = map(int, input().split())
num = input()

stack = [num[0]]

for i in range(1, N):
    while stack and K > 0:
        if stack[-1] < num[i]:
            stack.pop()
            K -= 1
        else:
            break
    stack.append(num[i])

if K:
    print(''.join(map(str, stack[:-K])))
else:
    print(''.join(map(str, stack)))