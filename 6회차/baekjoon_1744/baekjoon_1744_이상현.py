N = int(input())
positive = []
negative = []
result = 0

for _ in range(N):
    num = int(input())

    if num > 1:
        positive.append(num)
    elif num == 1:
        result += 1
    else:
        negative.append(num)

positive.sort(reverse = True)
negative.sort()

len_positive = len(positive)
len_negative = len(negative)

for i in range(0, len_positive, 2):
    if i + 1 >= len_positive:
        result += positive[i]
    else:
        result += positive[i] * positive[i + 1]

for i in range(0, len_negative, 2):
    if i + 1 >= len_negative:
        result += negative[i]
    else:
        result += negative[i] * negative[i + 1]

print(result)