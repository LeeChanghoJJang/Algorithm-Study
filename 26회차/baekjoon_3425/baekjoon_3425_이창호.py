import sys
sys.stdin =open('input.txt')
input = sys.stdin.readline

while True:
    operator = []
    while True:
        operator.append(input().strip())
        if operator[-1] == 'QUIT': quit()
        if operator[-1] == 'END': break

    for _ in range(int(input())):
        try:
            stack = [int(input())]
            for o in operator:
                if o == 'END': break
                if o[:3] == 'NUM':
                    stack.append(int(o[4:]))
                elif o == 'POP':
                    stack.pop()
                elif o == 'INV':
                    stack[-1] *= -1
                elif o == 'DUP':
                    stack.append(stack[-1])
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if o == 'SWP':
                        stack.append(a)
                        stack.append(b)
                    elif o == 'ADD':
                        stack.append(a + b)
                    elif o == 'SUB':
                        stack.append(b - a)
                    elif o == 'MUL':
                        stack.append(a * b)
                    elif o == 'DIV':
                        if b / a < 0:
                            stack.append((abs(b) // abs(a)) * -1)
                        else:
                            stack.append(abs(b) // abs(a))
                    elif o == 'MOD':
                        if b < 0:
                            stack.append((abs(b) % abs(a)) * -1)
                        else:
                            stack.append(abs(b) % abs(a))
                if stack and abs(stack[-1]) > 10 ** 9: raise
            if len(stack) != 1: raise
        except:
            stack = ['ERROR']
        print(stack[0])

    print()
    input()
