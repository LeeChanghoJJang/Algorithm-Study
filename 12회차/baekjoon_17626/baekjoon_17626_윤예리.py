# 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다.

n = int(input())
square = [] # 제곱수
for i in range(1, n+1):
    if i % (i ** 0.5) == 0:
        # n이 제곱수인 경우
        if n == i:
            exit(print(1))
        square.append(i)

l = len(square)
# 2개의 합
for i in range(l):
    for j in range(l):
        if square[i] + square[j] == n:
            exit(print(2))

# 3개의 합
for i in range(l):
    for j in range(l):
        for k in range(l):
            if square[i] + square[j] + square[k] == n:
                exit(print(3))

print(4)
