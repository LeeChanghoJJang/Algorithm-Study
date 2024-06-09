import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input())
crime = list(map(int,sys.stdin.readline().split()))
R = [list(map(int,input().split())) for _ in range(N)]
mapia = int(input()) # 마피아

deq = deque()
survivors = (1<<N) - 1 # 모든 플레이어가 생존한 상태
dp = {} # dp에 survivors에 따른 방문여부 저장
answer = 0 # 최대 생존시간

# 플레이어 수가 홀수인 경우, 낮부터 시작
if N%2 !=0:
    vote_victim = crime.index(max(crime))
    if vote_victim == mapia: # 플레이어가 마피아인경우
        exit(print(0))
    else:
        survivors = survivors & ~ (1<<vote_victim)
        crime[vote_victim] = float('-inf')

# 초기 상태를 큐에 추가
deq.append((survivors,crime,0))

while deq:
    survivors,crime,nights = deq.popleft()
    # 마피아가 낮에 유죄 지수가 가장 높은지 확인하고, 그렇다면 answer 업데이트
    if (crime.index(max(crime)) == mapia) & (nights != 0):
        answer = max(answer,nights)
    elif survivors not in dp:
        dp[survivors] = 1 # 현재 상태를 방문한 거으로 표시
        if nights !=0:
            vote_victim = crime.index(max(crime))
            survivors = survivors & ~(1<< vote_victim)
            crime[vote_victim] = float('-inf')

        for i in range(N):
            if (i != mapia) & (survivors & (1<<i) !=0):
                if survivors & ~(1<<i) not in dp:
                    _crime = [j for j in crime]
                    _crime[i] = float('-inf')
                    for j in range(N):
                        _crime[j] = _crime[j] + R[i][j]
                    deq.appendleft((survivors & ~(1<<i),_crime,nights+1))

print(answer)
