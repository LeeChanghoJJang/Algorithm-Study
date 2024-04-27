# 백준 1744번 수 묶기

N = int(input())
positive = []
negative = []
result = 0

# 1보다 큰 양수와 1보다 작은 수를 따로 저장
# 1은 따로 더해주는게 최대값을 가짐
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

# positive의 경우 내림차순으로 정렬 후 큰 값끼리 곱해주고
# 만약 짝이 없는 경우 그냥 더해줌
for i in range(0, len_positive, 2):
    if i + 1 >= len_positive:
        result += positive[i]
    else:
        result += positive[i] * positive[i + 1]

# negative의 경우 오름차순으로 정렬 후 작은 값끼리 곱해주고(음수와 음수의 곱은 양수)
# 만약 짝이 없는 경우 그냥 더해줌
for i in range(0, len_negative, 2):
    if i + 1 >= len_negative:
        result += negative[i]
    else:
        result += negative[i] * negative[i + 1]

print(result)