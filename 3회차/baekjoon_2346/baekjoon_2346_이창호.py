import sys
sys.stdin = open('input.txt')
from collections import deque
N = int(input())
balloons = deque(enumerate(map(int,input().split()),start=1))

while balloons:
    num, move = balloons.popleft()
    print(num,end=' ')
    print(balloons)
    if move > 0:
        balloons.rotate(-move+1)
    else:
        balloons.rotate(-move)