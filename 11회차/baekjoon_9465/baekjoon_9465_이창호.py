import sys
sys.stdin = open('input.txt')  # 입력을 파일에서 읽도록 설정

for tc in range(int(input())):  # 테스트 케이스의 개수를 입력 받음
    N = int(input())  # 열의 개수를 입력 받음
    DP = [[0]*N for _ in range(2)]  # 동적 계획법을 위한 2차원 배열 초기화
    temp = [list(map(int,input().split())) for _ in range(2)]  # 각 행의 점수를 입력 받음
    for i in range(N):
        if i >= 2:  # 현재 열이 2 이상인 경우
            # 현재 열에서 위쪽 스티커를 선택했을 때의 최대 점수와 아래쪽 스티커를 선택했을 때의 최대 점수 중 더 큰 값을 선택하여 현재 열에 저장
            DP[0][i] = temp[0][i] + max(DP[1][i - 1], DP[1][i - 2])
            DP[1][i] = temp[1][i] + max(DP[0][i - 1], DP[0][i - 2])
        elif i == 0:  # 첫 번째 열인 경우
            DP[0][i] = temp[0][i]  # 첫 번째 열의 위쪽 스티커 점수를 그대로 저장
            DP[1][i] = temp[1][i]  # 첫 번째 열의 아래쪽 스티커 점수를 그대로 저장
        elif i == 1:  # 두 번째 열인 경우
            # 두 번째 열에서 위쪽 스티커를 선택했을 때의 점수와 아래쪽 스티커를 선택했을 때의 점수를 저장
            DP[0][i] = temp[0][i] + temp[1][i - 1]
            DP[1][i] = temp[1][i] + temp[0][i - 1]
    # 마지막 열에서 위쪽 스티커를 선택했을 때의 점수와 아래쪽 스티커를 선택했을 때의 점수 중 더 큰 값이 최대 점수
    print(max(DP[0][-1],DP[1][-1]))
