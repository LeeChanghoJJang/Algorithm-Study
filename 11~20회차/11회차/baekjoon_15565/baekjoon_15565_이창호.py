import sys
sys.stdin = open('input.txt')
N, K = map(int, input().split())
dolls = list(map(int, input().split()))

# 초기 설정
left = 0  # 구간의 시작 인덱스
count = 0  # 라이언 인형의 개수
min_length = float('inf')

for right in range(N):
    if dolls[right] == 1:
        count += 1

    # 라이언 인형의 개수가 K 이상인 경우
    if count >= K:
        # 왼쪽 포인터를 움직여 최소 길이를 구함
        while dolls[left] != 1 or count > K:
            if dolls[left] == 1:
                count -= 1
            left += 1

        min_length = min(min_length, right - left + 1)

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)
