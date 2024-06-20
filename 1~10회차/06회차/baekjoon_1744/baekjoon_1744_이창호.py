import sys
sys.stdin = open('input.txt')

N = int(input())
# 양수만 모음
positive_number = []
# 음수만 모음 
negative_number = []
# 양수와 음수를 분류하여 모아놓음
for i in range(N):
    num = int(input())
    if num > 0:
        positive_number.append(num)
    else:
        negative_number.append(num)
# 절대값이 높은 순으로 정렬
positive_number.sort(reverse=True)
negative_number.sort()
# 결과값 저장할 변수
ans = 0
# 양수들부터 2칸씩 
for i in range(1,len(positive_number),2):
    # 더한값보다 곱한값이 큰 경우에는 곱한값을 ans에 저장
    if positive_number[i] + positive_number[i-1] < positive_number[i] * positive_number[i-1]:
        ans += positive_number[i] * positive_number[i-1]
    else:
        ans += positive_number[i] + positive_number[i-1]
# 만약 길이가 홀수여서 한개가 남으면 남은것은 그냥 더해줌 
if len(positive_number) %2 ==1:
    ans += positive_number[-1]
# 음수들부터 2칸씩
for i in range(1,len(negative_number),2):
    if negative_number[i] + negative_number[i-1] < negative_number[i] * negative_number[i-1]:
        ans += negative_number[i] * negative_number[i-1]
    else:
        ans += negative_number[i] + negative_number[i-1]
# 길이가 홀수여서 한개가 남으면 남은 것은 그냥 더해줌
if len(negative_number) % 2 ==1:
    ans += negative_number[-1]

print(ans)
