import sys
sys.stdin = open('input.txt')

# 입력 받기
arr = list(input().split('-'))

# 첫 번째 숫자는 더하고 시작
result = sum(map(int, arr[0].split('+')))

# 나머지 숫자들은 빼줌
for i in arr[1:]:
    result -= sum(map(int, i.split('+')))

# 결과 출력
print(result)
