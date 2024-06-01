# import sys

# n, k = map(int, input().split())

# count = 0

# while bin(n).count('1') > k:
#     n = n+1
#     count = count +1

# print(count)

n, k = map(int, input().split())
answer = 0
while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1') # 1이 오른쪽에서 몇 번째에 있는지 찾기
    answer += 2 ** idx # 2 ^ (idx) 만큼 더하기
    n += 2 ** idx # 2 ^ (idx) 만큼 더하기
print(answer)