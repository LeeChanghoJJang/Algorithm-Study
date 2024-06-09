# 1. 참가자는 두 그룹으로 나누어진다. 한 그룹은 마피아이고, 또 다른 그룹은 시민이다.
# 1-1 마피아의 정체는 시민에게 알려져 있지 않다.

# 2. 참가자가 짝수 명 남았을 떄는 밤이다. 밤에는 마피아가 죽일 사람 한 명을 고른다.
# 2-1. 죽은 경우 arr[i][j] 만큼 유죄지수가 변한다. 

# 3. 참가자가 홀수 명 남았을 떄는 낮이다. 낮에는 참가자들이 가장 죄가 있을 것 같은 사람 한명을 죽인다.
# 3-1. 낮에 사람이 죽으면 유죄지수는 바뀌지 않는다.
# 3-2. 동률일 경우 번호가 가장 작은 사람이 죽는다.

# 4. 마피아가 한명도 남지 않았거나, 시민이 한명도 남지 않았다면 게임은 종료된다.
import sys

input = sys.stdin.readline


def backtrack(idx=0,dead=[]):
    global cnt
    target = -1
    # 낮
    if (N-len(dead))%2:
        tmp, target = -float('inf'),-1
        for i in range(N):
            if i not in dead and tmp < point[i]:
                target = i
                tmp = point[i]
    # 마피아 혼자 남았거나, 마피아가 타겟이 된 경우 게임은 끝남 
    if idx==N-1 or target==mafia:
        cnt = max(cnt,idx)
        return
    # 밤
    for i in range(N):
        if i != target and i not in dead and i != mafia :
            for j in range(N):
                point[j] += arr[i][j]
            if target == -1:
                backtrack(idx+1, dead+[i])
            else :
                backtrack(idx+1, dead+[target,i])
            for j in range(N):
                point[j] -= arr[i][j]
    

N = int(input())
point = [*map(int,input().split())]
arr = [[*map(int,input().split())] for _ in range(N)]
mafia = int(input())
cnt = 0
backtrack()
print(cnt)