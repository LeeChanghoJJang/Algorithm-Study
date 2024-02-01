# 백준 1476번 날짜 계산

# 방법1과 방법2는 똑같이 1부터 시작해서 우리가 알고 있는 연도와
# E S M 연도를 서로 비교 후 값이 같으면 출력
# 방법1은 input 값을 변수 하나에 문자열로 저장함

input_ = input()
year = 0

while f'{year % 15 + 1} {year % 28 + 1} {year % 19 + 1}' != input_:
    year += 1

print(year + 1)

#-----------------------------------------------------

# E, S, M = map(int, input().split())
# n = 1

# while True:

#     if not((n - E) % 15 or (n - S) % 28 or (n - M) % 19):
#         print(n)
#         break
#     n += 1

#-----------------------------------------------------

# 방법3: 연립합동식 공식 사용

# E, S, M = map(int, input().split())

# N1 = E * 28 * 19 * 13
# N2 = S * 15 * 19 * 17
# N3 = M * 15 * 28 * 10
# result = (N1 + N2 + N3) % (15 * 28 * 19)

# print(result if result != 0 else 7980)