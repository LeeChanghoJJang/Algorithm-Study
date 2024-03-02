import sys
sys.stdin = open('input.txt')

def f():
    cnt = sum(1>sum(bingo[i : 25 : 5]) for i in range(5))  # 가로
    cnt += sum(1>sum(bingo[i*5 : i*5+5]) for i in range(5))  # 세로
    cnt += (sum(bingo[i*5+i] for i in range(5)) < 1)  # 대각
    cnt += (sum(bingo[(4-i)*5+i] for i in range(5)) < 1)  # 대각
    return cnt

(*bingo,) = map(int, sys.stdin.read().split())

for i in range(25):
    bingo[bingo.index(bingo[25+i])] = 0
    (f() > 2) and exit(print(i+1))