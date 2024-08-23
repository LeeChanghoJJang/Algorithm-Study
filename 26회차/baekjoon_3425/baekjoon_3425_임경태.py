# 3425 고스택

def exec(commands, num):
    stack = [num]
    MAX_VAL = 10**9

    for cmd in commands:
        # NUM X: X를 스택의 가장 위에 저장
        if cmd[:3] == "NUM":
            n = int(cmd[4:])
            stack.append(n)

        # 스택이 비어 있는 경우에는 다른 명령어를 수행할 수 없으므로 에러 반환
        elif not stack:
            return "ERROR"

        # POP: 스택 가장 위의 숫자를 제거
        elif cmd == "POP":
            stack.pop()

        # INV: 첫 번째 수의 부호를 바꿈
        elif cmd == "INV":
            stack[-1] *= -1

        # DUP: 첫 번째 숫자를 하나 더 스택의 가장 위에 저장
        elif cmd == "DUP":
            stack.append(stack[-1])

        # 스택의 크기가 2 미만일 경우 에러 반환
        elif len(stack) < 2:
            return "ERROR"

        # SWP: 첫 번째 숫자와 두 번째 숫자의 위치를 서로 바꿈
        elif cmd == "SWP":
            stack[-1], stack[-2] = stack[-2], stack[-1]  # 스택의 상위 두 숫자의 위치를 바꿈

        # ADD, SUB, MUL, DIV, MOD: 스택의 상위 두 숫자를 처리
        elif cmd in {"ADD", "SUB", "MUL", "DIV", "MOD"}:
            a, b = stack.pop(), stack.pop()

            # ADD: 두 숫자를 더함
            if cmd == "ADD":
                temp = b + a

            # SUB: 두 번째 숫자에서 첫 번째 숫자를 뺌
            elif cmd == "SUB":
                temp = b - a

            # MUL: 두 숫자를 곱함
            elif cmd == "MUL":
                temp = b * a

            # 제수가 0인 경우 에러 반환
            elif cmd == "DIV":
                if a == 0:
                    return "ERROR"
                temp = abs(b) // abs(a)

                # 결과의 부호 결정
                if (a > 0 and b < 0) or (a < 0 and b > 0):
                    temp = -temp

            elif cmd == "MOD":
                if a == 0:
                    return "ERROR"
                temp = abs(b) % abs(a)
                # 피제수가 음수인 경우 결과의 부호 결정
                if b < 0:
                    temp = -temp

            # 계산 결과가 10^9를 넘으면 에러 반환
            if abs(temp) > MAX_VAL:
                return "ERROR"

            # 계산 결과를 스택에 추가
            stack.append(temp)
        else:
            return "ERROR"

    return stack[0] if len(stack) == 1 else "ERROR"

while True:
    commands = []

    while True:
        cmd = input()
        if cmd == "QUIT":
            quit()
        if cmd == "END":
            break
        commands.append(cmd)

    for _ in range(int(input())):
        num = int(input())
        print(exec(commands, num))

    print()
    input()