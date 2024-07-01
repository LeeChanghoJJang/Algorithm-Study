import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
number = input().strip()

num_to_remove = K
stack = []

for digit in number:
    if num_to_remove and stack and stack[-1] <digit:
        stack.pop()
        num_to_remove-=1
    stack.append(digit)

if num_to_remove >0:
    stack = stack[:-num_to_remove]

print(''.join(stack))