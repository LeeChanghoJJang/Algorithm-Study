import sys; input = sys.stdin.readline

# 아니...

def num(x):
    stack.append(x)

def pop():
    if not stack:
        return 1
    stack.pop()

def inv():
    if not stack:
        return 1
    stack[-1] = -stack[-1]

def dup():
    if not stack:
        return 1
    stack.append(stack[-1])

def swp():
    if len(stack) < 2:
        return 1
    stack[-1],stack[-2] = stack[-2],stack[-1]

def add():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if abs(a+b) > 1e9:
        return 1
    stack.append(a+b)

def sub():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if abs(b-a) > 1e9:
        return 1
    stack.append(b-a)

def mul():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if abs(a*b) > 1e9:
        return 1
    stack.append(a*b)

def div():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if a == 0:
        return 1    
    res = abs(b)//abs(a)
    if a<0:
        res = -res
    if b<0:
        res = -res
    stack.append(res)

def mod():
    if len(stack) < 2:
        return 1
    a = stack.pop()
    b = stack.pop()
    if a == 0:
        return 1
    res = abs(b) % abs(a)

    if b<0:
        res = -res
    stack.append(res)

commands = {
    "POP": pop,
    "INV": inv,
    "DUP": dup,
    "SWP": swp,
    "ADD": add,
    "SUB": sub,
    "MUL": mul,
    "DIV": div,
    "MOD": mod
}


while 1:
    cmd = []
    while 1:
        a, *data = input().strip().split()
        if a == "QUIT": exit()
        if a == "END": break
        cmd.append((a,data))

    for _ in range(int(input())):
        stack = [int(input())]
        for char, n in cmd:
            if char == "NUM":
                n = int(n[0])
                num(n)
            else:
                if commands.get(char)():
                    print("ERROR")
                    break
            
        else :
            if len(stack) == 1:
                print(*stack)
            else:
                print("ERROR")
    print()
    input()