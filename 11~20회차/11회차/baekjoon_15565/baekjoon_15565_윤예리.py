import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

size = end = cnt = 0
result = float('inf')

for start in range(n):
    # start부터 end까지 라이언의 개수가 k개가 되거나 end가 끝에 닿을 때 까지 sliding window에 추가해준다.
    while cnt < k and end < n:
        size += 1
        if arr[end] == 1:
            cnt += 1
        end += 1

    # 라이언이 k개면 결과값 갱신
    if cnt == k:
        if result > size:
            result = size
            
    # 다음 start로 시작하기 전에 cnt 계산
    # 슬라이딩 윈도우
    if arr[start] == 1:
        cnt -= 1
    size -= 1

if result == float('inf'):
    print(-1)
else:
    print(result)