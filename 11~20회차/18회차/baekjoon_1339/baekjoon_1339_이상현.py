import sys
sys.stdin = open('input.txt')

N = int(input())
dict_ = {chr(i): 0 for i in range(65, 91)}

for _ in range(N):
    word = input()[::-1]

    for i, char in enumerate(word):
        dict_[char] += 10 ** i

temp = sorted(filter(lambda x: x > 0, dict_.values()), reverse=True)
result = sum(w * (9 - i) for i, w in enumerate(temp))

print(result)