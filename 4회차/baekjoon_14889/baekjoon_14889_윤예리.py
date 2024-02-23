from itertools import combinations
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
a = [i for i in range(n)]
comb = list(combinations(a, n//2))      # 0, 1, 2, 3을 2개씩 조합
min_v = 30000

for c in comb:
    # 스타트 팀 능력치
    comb_2 = list(combinations(c, 2))   # 조합에서 또 2개씩 조합
    power_start = 0
    for c_2 in comb_2:
        power_start += s[c_2[0]][c_2[1]] + s[c_2[1]][c_2[0]]

    # 링크 팀 능력치
    b = [i for i in range(n)]
    for _ in c:
        b.pop(b.index(_))       # 남은 번호 확인
    comb_3 = list(combinations(b, 2))   # 남은 번호에서 2개씩 조합
    power_link = 0
    for c_3 in comb_3:
        power_link += s[c_3[0]][c_3[1]] + s[c_3[1]][c_3[0]]

    if abs(power_start-power_link) < min_v:
        min_v = abs(power_start-power_link)
print(min_v)