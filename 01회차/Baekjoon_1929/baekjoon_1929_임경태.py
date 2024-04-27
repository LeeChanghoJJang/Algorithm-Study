# 1929 소수 구하기
# M ~ N 사이의 소수 구하기
# 에라토스테네스의 체
# 1. 수 나열 -> 인덱스를 수로 간주하는 배열 생성
# 2. 자기 자신을 제외하고 배수를 지우는 반복문 생성
# 2-1. 반복문은 sqrt(N) 보다 큰 소수 중 가장 최소값에 다다랐을 때 중지
# 2-2. 수를 증가시키는 반복문 + 소수를 판별하고 그 배수를 제거하는 반복문
# 3. 배열에서 지운 수 빼고 남은 수를 출력

M, N = map(int, input().split())
numbers = [0, 0] + [1] * (N-1)

for num in range(2, int(N**0.5)+1):  # 2에서 sqrt(N) 이하까지 순회
    if numbers[num]:
        for i in range(2*num, N+1, num):  # 자신을 제외한 배수를 0으로 변환
            numbers[i] = 0

for i in range(M, N+1):  # 범위 내에서 출력
    if numbers[i]:
        print(i)


''' 시간 초과 코드
import sys
M, N = map(int,sys.stdin.readline().split())
if M == 1: M = 2
for num in range(M, N+1):
    for divider in range(2, (num // 2) + 1):
        if num % divider == 0:
            break
    else:
        print(num)
'''