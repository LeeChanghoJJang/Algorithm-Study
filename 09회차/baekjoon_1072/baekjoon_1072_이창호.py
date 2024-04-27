import sys
import math
sys.stdin = open('input.txt')

# 입력 받기
X,Y = map(int,input().split())

# 현재 승률 계산
now = int(Y*100/X)

# 목표 승률 설정 (현재 승률에서 1% 증가)
target = now + 1

# 목표 승률이 0 초과 100 미만인 경우
if 0 < target < 100:
    # 게임 횟수 계산
    added = ((Y - X) * 100) / (target-100) - X
else:
    # 목표 승률이 0 또는 100인 경우, 게임 횟수를 증가시킬 수 없음
    print(-1)
    exit()

# 최소 게임 횟수 계산 및 출력
print(max(1,math.ceil(added)))
