'''
문제
성냥개비는 숫자를 나타내기에 아주 이상적인 도구이다. 보통 십진수를 성냥개비로 표현하는 방법은 다음과 같다.



성냥개비의 개수가 주어졌을 때, 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 큰 수를 찾는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개 이다. 각 테스트 케이스는 한 줄로 이루어져 있고, 성냥개비의 개수 n이 주어진다. (2 ≤ n ≤ 100)

출력
각 테스트 케이스에 대해서 입력으로 주어진 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 가장 큰 수를 출력한다. 두 숫자는 모두 양수이어야 하고, 숫자는 0으로 시작할 수 없다. 

예제 입력 1 
4
3
6
7
15
예제 출력 1 
7 7
6 111
8 711
108 7111111
'''






import sys
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
