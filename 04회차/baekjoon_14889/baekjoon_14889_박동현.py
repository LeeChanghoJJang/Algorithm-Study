import sys
from itertools import combinations


t = int(input())

start_link = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(t)]
member = set(range(t))
teams = list(combinations(range(t), t//2))  # 부분집합을 만들어 브루트포스
teams = teams[:len(teams)//2]               # 부분집합 반만 하면 나머지는 대칭
synergy = []
tt = t//2
for team in teams :
    enemy = list(member - set(team))        # 대칭인 부분집합 설정
    output = 0 
    e_output = 0
    for i in range(tt):
        for j in range(tt):
            output += start_link[team[i]][team[j]]
            e_output += start_link[enemy[i]][enemy[j]]

    synergy.append(abs(e_output-output))    # 차이를 담아두기

synergy.sort()
print(synergy[0])

# input() 56980kb / 3128ms
# stdin.readline() 56980kb /3096ms
# 그냥 느리네..