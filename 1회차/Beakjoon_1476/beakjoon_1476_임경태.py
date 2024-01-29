# 백준 1476번 날짜 계산
# E, S, M 세 수는 서로 다른 범위를 가짐 (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
# E S M으로 표시되는 가장 빠른 연도를 출력
# 지난 연도가 n이라고 할 때
# E = n % 15, S = n % 28 , M = n % 19

E, S, M = map(int, input().split())
year = 1

# 세 수의 나머지가 모두 0이 되는 연도 찾기
while (year-E) % 15 != 0 or (year-S) % 28 != 0 or (year-M) % 19 != 0:
    # 조건 만족 안하면 1 계속 증가
    year += 1

print(year)