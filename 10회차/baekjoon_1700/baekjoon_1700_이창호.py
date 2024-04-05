import sys
sys.stdin = open('input.txt')  # input.txt 파일을 표준 입력으로 사용

from collections import Counter

# 멀티탭의 개수 N과 사용 순서의 길이 K를 입력받습니다.
N, K = map(int, input().split(' '))

# 사용 순서를 입력받아 리스트 use에 저장합니다.
use = list(map(int, input().split(' ')))

code = []  # 현재 꽂혀있는 코드를 저장할 리스트
answer = 0  # 멀티탭 빈 횟수를 저장할 변수

for this in range(K):
    if use[this] in code:  # 이미 꽂혀져 있는 코드라면 건너뜁니다.
        continue

    if len(code) < N:  # 멀티탭에 자리가 남아 있다면,
        code.append(use[this])  # 코드를 꽂습니다.
        continue

    priority = []
    for c in code:  # 현재 꽂혀 있는 코드들에 대해 우선순위를 계산합니다.
        if c in use[this:]:  # 다음에 또 이용해야 한다면,
            priority.append(use[this:].index(c))  # 다음 사용 순서까지의 인덱스를 우선순위로 설정합니다.
        else:
            priority.append(101)  # 사용 순서에 더 이상 등장하지 않는다면 우선순위를 매우 높게 설정합니다.
    target = priority.index(max(priority))  # 우선순위가 가장 높은 코드를 타겟으로 선택합니다.
    code.remove(code[target])  # 타겟 코드를 제거하고,
    code.append(use[this])  # 현재 코드를 꽂습니다.
    answer += 1  # 멀티탭 빈 횟수를 증가시킵니다.

# 최종적으로 구한 답을 출력합니다.
print(answer)
