import sys
sys.stdin = open('input.txt')
# deque을 써서 회전을 손쉽게 활용하자.
from collections import deque
N = int(input())
# 당시의 인덱스와 값을 한쌍으로 저장시켜놓자
balloons = deque(enumerate(map(int,input().split()),start=1))
# balloons에서 순서대로 pop을 하자
while balloons:
    print(balloons)
    # 풍선의 번호와 터트리면 이동횟수를 저장
    num, move = balloons.popleft()
    # 일단 터트린 번호 출력
    print(num,end=' ')
    # 양수일 때에는 왼쪽끝에서 오른쪽끝으로 이동
    if move > 0:
        # 터트리면 이동에 상관있는 1개 풍선이 빠져서, 1칸 덜 이동 해야함
        balloons.rotate(-move+1)
    # 음수일 때에는 오른쪽 끝에서 왼쪽 끝으로 이동
    else:
        # 터트리면 뒤에서 앞으로 이동하기 때문에 이동에 상관없는 1개 풍선이 빠짐
        # 주어진 만큼만 이동하면 됨
        balloons.rotate(-move)
