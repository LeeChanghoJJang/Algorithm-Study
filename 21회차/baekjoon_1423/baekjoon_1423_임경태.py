# 1423 원숭이 키우기
def solution():
    sum_str = 0
    DP = [0] * (D+1)

    # 초기 총 힘의 합 계산 및 레벨 조정
    for i in range(1, N+1):
        sum_str += char_lvl[i] * char_str[i]
        char_lvl[i] = min(D, char_lvl[i])

    # DP 배열 업데이트를 통해 최대 힘의 합 계산
    for i in range(1, N+1):
        while char_lvl[i] > 0:
            char_lvl[i] -= 1
            for j in range(D, -1, -1):
                # 다음 레벨의 캐릭터 탐색
                for k in range(i+1, N+1):
                    if k+j-i <= D:
                        # 새로운 힘의 합 계산 및 최대값 갱신
                        DP[k+j-i] = max(DP[k+j-i], DP[j] + char_str[k] - char_str[i])

    return DP[D] + sum_str


N = int(input())
char_lvl = [0] + list(map(int, input().split()))
char_str = [0] + list(map(int, input().split()))
D = int(input())

print(solution())