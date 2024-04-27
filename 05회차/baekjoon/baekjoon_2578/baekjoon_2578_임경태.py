import sys
sys.stdin = open('input.txt')

def f():
    cnt = sum(1 > sum(bingo[i : 25 : 5]) for i in range(5))  # 가로
    cnt += sum(1 > sum(bingo[i*5 : i*5+5]) for i in range(5))  # 세로
    cnt += (sum(bingo[i*5+i] for i in range(5)) < 1)  # 대각
    cnt += (sum(bingo[(4-i)*5+i] for i in range(5)) < 1)  # 대각
    return cnt

# sys.stdin.read() : 입력 EOF까지의 모든 내용을 하나의 문자열로 반환
# (*bingo,) : 튜플 언패킹을 사용하여, map() 함수의 반환 값을 첫 번째 요소에만 할당
(*bingo,) = map(int, sys.stdin.read().split())
'''
print(bingo)
>> [11, 12, 2, 24, 10, 16, 1, 13, 3, 25, 6, 20, 5, 21, ...]
'''

for i in range(25):
    bingo[bingo.index(bingo[25+i])] = 0
    # 단축 평가 실행
    (f() > 2) and exit(print(i+1))