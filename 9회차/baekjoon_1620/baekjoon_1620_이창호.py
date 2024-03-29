import sys
from collections import Counter
sys.stdin = open('input.txt')

# 포켓몬의 수 N과 문제의 수 T 입력 받기
N, T = map(int,input().split())

# 모든 줄을 읽어와서 리스트에 저장
totals = sys.stdin.readlines()

# N개의 포켓몬 이름 추출
pocketmon = list(map(lambda x : x.strip(), Counter(totals[:N]).keys()))

# 포켓몬 이름에 해당하는 번호 부여
numbers = range(1,N+1)
pocket_to_num= dict(zip(pocketmon,numbers)) # 포켓몬 이름을 번호로 매핑하는 딕셔너리
num_to_pocket = dict(zip(numbers,pocketmon)) # 번호를 포켓몬 이름으로 매핑하는 딕셔너리

# T개의 문제에 대한 답 출력
for i in list(map(lambda x:x.strip(),totals[N:])):
    if i.strip().isdigit(): # 입력이 숫자인 경우
        # 해당 번호에 대응하는 포켓몬 이름 출력
        print(num_to_pocket[int(i.strip())].strip())
    else:
        # 해당 포켓몬 이름에 대응하는 번호 출력
        print(pocket_to_num[i])
