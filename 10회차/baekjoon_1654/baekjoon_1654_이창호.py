import sys
sys.stdin = open('input.txt')  # input.txt 파일을 표준 입력으로 사용

# 랜선의 개수 K와 필요한 랜선의 개수 N을 입력받습니다.
K, N = map(int, input().split())

# 각 랜선의 길이를 입력받아 리스트 arr에 저장합니다.
arr = [int(input()) for _ in range(K)]

start = 1  # 랜선의 길이는 최소 1이므로 시작점을 1로 설정합니다.
end = max(arr)  # 랜선의 최대 길이를 끝점으로 설정합니다.

result = 0  # 결과값을 저장할 변수를 초기화합니다.

# 이분 탐색을 수행합니다.
while start <= end:
    mid = (start + end) // 2  # 중간 길이를 계산합니다.

    # 중간 길이로 랜선을 자를 때 만들어진 랜선의 개수를 계산합니다.
    # 나눗셈 연산을 최적화하기 위해 리스트 컴프리헨션을 사용합니다.
    count = sum(length // mid for length in arr)

    # 만들어진 랜선의 개수가 필요한 랜선의 개수보다 작다면,
    if count < N:
        end = mid - 1  # 랜선의 길이를 줄여서 다시 탐색합니다.
    else:
        result = mid  # 결과를 갱신하고
        start = mid + 1  # 랜선의 길이를 늘려서 다시 탐색합니다.

# 최종적으로 구한 결과값을 출력합니다.
print(result)
