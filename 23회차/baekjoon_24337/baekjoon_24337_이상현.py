import sys
sys.stdin = open('input.txt')

N, a, b = map(int, input().split())
list_ = []

for i in range(1, a):
    list_.append(i)

list_.append(max(a, b))

for i in range(b - 1, 0, -1):
    list_.append(i)

len_ = len(list_)

if len(list_) > N:
    print(-1)

else:
    print(list_[0], end=" ")

    for i in range(N - len_):
        print(1, end=" ")

    for i in range(1, len_):
        print(list_[i], end=" ")