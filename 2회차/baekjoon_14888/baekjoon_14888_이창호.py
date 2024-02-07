from collections import deque
import sys
sys.stdin = open('input.txt')
# def cal(now, operators):
#     queue =deque()
#     queue.append(now[0])
#
#     for i in range(1,len(now)):
#         queue.append(operators[i-1])
#         queue.append(now[i])
#     stack =[]
#
#     print(queue)
#     for token in queue:
#         if type(token) ==int:
#             stack.append(token)
#         elif len(stack) >=2:
#             b = stack.pop()
#             a = stack.pop()
#             if token == '+':
#                 stack.append(a + b)
#             elif token == '-':
#                 stack.append(a - b)
#             elif token == '*':
#                 stack.append(a * b)
#             elif token == '/':
#                 stack.append(int(a / b))  # 정수 나눗셈으로 몫만 취함
#     return stack[0]
# def backtracking(N,now,operators,numbers):
#     global max_val
#     global min_val
#
#     if len(now) == N:
#         print(now)
#         result = cal(now,operators)
#         max_val = max(max_val, result)
#         min_val = min(min_val, result)
#         return None
#
#     for i in numbers:
#         if len(now)==0 or i not in now:
#             now.append(i)
#             backtracking(N,now,operators,numbers)
#             now.pop()
#
# N = int(input())
# numbers = list(map(int, input().split()))
# operator_counts = list(map(int, input().split()))
# now= deque()
# operators = deque()
# max_val = float('-inf')
# min_val = float('inf')
# for op, count in zip("+-*/", operator_counts):
#     operators.extend([op] * count)
#
# backtracking(N,now,operators,numbers)
# print(max_val)
# print(min_val)

from collections import deque

def cal(now, operators):
    queue = deque()
    queue.append(now[0])

    for i in range(1, len(now)):
        queue.append(operators[i - 1])
        queue.append(now[i])
    stack = []

    for token in queue:
        if type(token) == int:
            stack.append(token)
        elif len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # 정수 나눗셈으로 몫만 취함
    return stack[0]

def backtracking(N, now, operators, numbers):
    global max_val
    global min_val

    if len(now) == N * 2 - 1:
        result = cal(now, operators.copy())  # operators를 복사하여 원본 유지
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return None

    for i in range(len(operators)):
        now.append(operators.popleft())
        backtracking(N, now, operators, numbers)
        operators.append(now.pop())

# 사용자 입력
N = int(input())
numbers = list(map(int, input().split()))
operator_counts = list(map(int, input().split()))
now = deque()
operators = deque()
max_val = float('-inf')
min_val = float('inf')
for op, count in zip("+-*/", operator_counts):
    operators.extend([op] * count)

backtracking(N, now, operators, numbers)

print("최대값:", max_val)
print("최소값:", min_val)
