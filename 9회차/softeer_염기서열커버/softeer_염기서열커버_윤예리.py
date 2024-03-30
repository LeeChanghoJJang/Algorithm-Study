n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
# '.'의 개수가 적은 순서대로 정렬
arr.sort(key=lambda x:x.count('.'))

result = 0
while arr:
    # 처음 하나를 뽑아서 만족할 수 있는 염기서열이 있는지 확인
    seq = arr.pop(0)
    # 서열 수 + 1
    result += 1

    idx = []

    for i in range(len(arr)):
        # 염기서열의 길이만큼 확인
        cnt = 0
        for j in range(m):
            if seq[j] == arr[i][j] or seq[j] == '.' or arr[i][j] == '.':
                cnt += 1
            else:
                break

        # 끝까지 확인 후 만족하는 cnt가 길이와 같다면 idx에 인덱스를 append
        if cnt == m:
            idx.append(i)

    # 만족하는 arr의 인덱스를 뒤에서부터 pop
    for i in reversed(idx):
        arr.pop(i)
print(result)