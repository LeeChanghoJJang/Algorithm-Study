import sys
sys.stdin = open('input.txt')

N = int(input())
positive_number = []
negative_number = []
for i in range(N):
    num = int(input())
    if num > 0:
        positive_number.append(num)
    else:
        negative_number.append(num)
positive_number.sort(reverse=True)
negative_number.sort()

ans = 0
for i in range(1,len(positive_number),2):
    if positive_number[i] + positive_number[i-1] < positive_number[i] * positive_number[i-1]:
        ans += positive_number[i] * positive_number[i-1]
    else:
        ans += positive_number[i] + positive_number[i-1]

if len(positive_number) %2 ==1:
    ans += positive_number[-1]

for i in range(1,len(negative_number),2):
    if negative_number[i] + negative_number[i-1] < negative_number[i] * negative_number[i-1]:
        ans += negative_number[i] * negative_number[i-1]
    else:
        ans += negative_number[i] + negative_number[i-1]

if len(negative_number) % 2 ==1:
    ans += negative_number[-1]

print(ans)