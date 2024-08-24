import sys
input = sys.stdin.readline

q = ''
while True:
    cmd = []
    if q:
        cmd.append(q)
    while True:
        c = input().strip()
        cmd.append(c)
        if c == 'END':
            cmd.append(c)
            c = ''
            break

    N = int(input())
    for _ in range(N):
        v = int(input())
        stack = [v]
        
        err = True
        for c in cmd:
            if c[0] == 'N':
                c = c.split()
                n = int(c[1])
                stack.append(n)
            elif c == 'END':
                err = False
                continue
            elif c == 'POP':
                if not stack:
                    break
                stack.pop()
            elif c == 'INV':
                if not stack:
                    break
                stack.append(-stack.pop())
            elif c == 'DUP':
                if not stack:
                    break
                stack.append(stack[-1])
            else:
                if len(stack) < 2:
                    break
                elif c == 'SWP':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a)
                    stack.append(b)
                elif c == 'ADD':
                    a, b = stack.pop(), stack.pop()
                    if abs(a + b) > 1e9:
                        break
                    stack.append(a + b)
                elif c == 'SUB':
                    a, b = stack.pop(), stack.pop()
                    if abs(b - a) > 1e9:
                        break
                    stack.append(b - a)
                elif c == 'MUL':
                    a, b = stack.pop(), stack.pop()
                    if abs(a * b) > 1e9:
                        break
                    stack.append(a * b)
                elif c == 'DIV':
                    a, b = stack.pop(), stack.pop()
                    if not a:
                        break
                    if a * b < 0:
                        a = abs(a)
                        b = abs(b)
                        stack.append(-(b//a))
                        continue
                    stack.append(b // a)
                elif c == 'MOD':
                    a, b = stack.pop(), stack.pop()
                    if not a:
                        break
                    if b < 0:
                        c = -1
                    else:
                        c = 1
                    a = abs(a)
                    b = abs(b)
                    stack.append((b % a) * c)

        if err:
            print('ERROR')
            continue
        
        if len(stack) > 1 or not stack:
            print('ERROR')
            continue
        print(stack[0])
        
    space = input().strip()
    q = input().strip()
    if q == 'QUIT':
        break
    else:
        print()