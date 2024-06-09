n, k = map(int, input().split())
numbers = list(map(int, input()))
stack = [numbers[0]]

for i in range(1, len(numbers)):
    while stack and k > 0:
        if stack[-1] < numbers[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(numbers[i])

if k > 0:
    print(''.join(map(str, stack[:-k])))
else:
    print(''.join(map(str, stack)))