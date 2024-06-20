'''
더하기가 있으면 다 더한 뒤 식 계산
'''

from collections import deque

ls = list(input())

# num 이라는 리스트에 숫자와 연산자 나눠서 넣기
num = deque()
char = ''
for i in ls:
    if i.isdigit():
        char += i

    else:
        if char:
            num.append(int(char))
            char = ''
        num.append(i)
if char:
    num.append(int(char))
# print(num)

# num에 있는 숫자/연산자를 하나씩 빼서 계산
stack = deque()
while num:
    i = num.popleft()

    # 더하기가 나오면 더해서 stack에 append
    if i == '+':
        a = stack.pop()
        b = num.popleft()
        stack.append(a+b)

    elif i == '-':
        continue

    else:
        stack.append(i)

# 남은 애들을 앞에서부터 다 뺀다.
result = stack.popleft()
while stack:
    result -= stack.popleft()
print(result)