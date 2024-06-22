import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dp = [float('inf')]*101
init_list = ['', '', 1, 7, 4, 2, 6, 8]
for i in range(2, 8) :
  dp[i] = init_list[i]

for i in range(8, 101) :
  for j in range(2, i-1) :
    dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i-j])))
    if j == 6 :
      dp[i] = min(dp[i], int(str(dp[i-j]) + '0'))

def find_biggest(num) :
  result = '1'*(num // 2)
  if num % 2 :
    result = '7' + result[1:]
  return result

def find_smallist(num) :
  return dp[num]

T = int(input())
for _ in range(T) :
  N = int(input())
  print(find_smallist(N),  find_biggest(N))
