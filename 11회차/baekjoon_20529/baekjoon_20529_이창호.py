import sys
from itertools import combinations
from collections import Counter
sys.stdin = open('input.txt')  # 입력을 파일에서 읽도록 설정

# 두 MBTI 문자열의 차이(거리)를 계산하는 함수
def compared(A, B):
    return sum(1 for i in range(len(A)) if A[i] != B[i])

T = int(input())  # 테스트 케이스의 개수를 입력 받음

for tc in range(T):
    N = int(input())  # MBTI 문자열의 개수를 입력 받음
    arr = sys.stdin.readline().split()  # MBTI 문자열을 공백을 기준으로 분리하여 리스트로 저장

    # 각 MBTI의 개수를 카운트하는 Counter 객체 생성
    counts = Counter(arr)

    # 각 MBTI 조합의 거리를 저장할 딕셔너리 초기화
    dist = dict()

    # 최소 거리를 저장할 변수 초기화
    min_value = float('inf')

    # MBTI 문자열의 개수가 32보다 크면 불가능한 경우이므로 바로 0 출력 후 다음 테스트 케이스로 이동
    if N > 32:
        print(0)
        continue

    # 모든 MBTI 조합에 대해 반복
    for A, B, C in combinations(arr, 3):
        # 이미 계산된 거리인지 확인 후, 계산되지 않은 경우 거리를 계산하여 딕셔너리에 저장
        if (A, B, C) not in dist.keys():
            dist[(A, B, C)] = compared(A, B) + compared(B, C) + compared(A, C)
            # 최소 거리 업데이트
            min_value = min(min_value, dist[(A, B, C)])

        # 해당 MBTI 조합에서 어떤 MBTI가 3개 이상 있는지 확인하여 최소 거리를 0으로 설정하고 반복문 종료
        if any(counts[mbti] >= 3 for mbti in [A, B, C]):
            min_value = 0
            break

        # 이미 충분한 조합을 찾은 경우 추가적인 계산을 하지 않고 반복문 종료
        if len(dist) > 833:
            break

    # 최소 거리 출력
    print(min_value)

''' 
    겹치는 아이템 수가 2개인 경우 : 3C2 * 13C1 + 3C1*13C2 = 273
    안겹치는 경우 : 16C3 =560      
'''
