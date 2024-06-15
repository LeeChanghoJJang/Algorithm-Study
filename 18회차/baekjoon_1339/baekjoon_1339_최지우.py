n = int(input())

char = {i: 0 for i in range(27)}

for _ in range(n):
    t = input()[::-1]
    for i in range(len(t)):
        char[ord(t[i])-65] += 10**i

result = 0
k = 9
for num in sorted(char.values(), key=lambda x: -x):
    if not num:
        break

    result += k * num
    k -= 1

print(result)