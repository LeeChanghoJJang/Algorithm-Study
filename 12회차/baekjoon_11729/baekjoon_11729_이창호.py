import sys

# 표준 입력을 'input.txt'에서 읽도록 재지정
sys.stdin = open('input.txt')


# 하노이 탑 문제를 해결하는 재귀 함수
def hanoi(n, start, end):
    # 기본 경우: 디스크가 하나만 있는 경우, 시작 기둥에서 끝 기둥으로 이동
    if n == 1:
        print(start, end)  # 시작 기둥에서 끝 기둥으로 디스크 이동
        return

    # 시작 기둥에서 남은 n-1개의 디스크를 보조 기둥으로 이동
    hanoi(n - 1, start, 6 - start - end)

    # 시작 기둥에서 가장 큰 디스크를 끝 기둥으로 이동
    print(start, end)

    # 보조 기둥에서 남은 n-1개의 디스크를 끝 기둥으로 이동
    hanoi(n - 1, 6 - start - end, end)


# 표준 입력에서 디스크의 개수를 읽음
n = int(input())

# 문제를 해결하는 데 필요한 총 이동 횟수를 계산하고 출력
print(2 ** n - 1)

# 하노이 함수를 호출하여 하노이 탑 문제를 해결
hanoi(n, 1, 3)
