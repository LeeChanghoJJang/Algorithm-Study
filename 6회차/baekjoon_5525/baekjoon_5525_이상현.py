import sys
input = sys.stdin.readline

# 백준 5525번 IOIOI

N = int(input())
input()
S = input().strip('O').split('I')
dict_ = {}
temp = result = 0

for elem in S:
    if elem == 'O':
        temp += 1
    else:
        if temp in dict_:
            dict_[temp] += 1
        else:
            dict_[temp] = 1
        temp = 0

for key, value in dict_.items():
    if key >= N:
        result += (key - N + 1) * value

print(result)