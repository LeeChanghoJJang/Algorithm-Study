# 순차적으로 포함 되고 안되고 하면서 s랑 합이 같은지 확인

def backtraking(i, total):
    global cnt
    # print(total)
    if total == s and i > 0:  # 합이 같으면 카운트에 1 더하기
        cnt += 1

    for j in range(i, n):
        total += arr[j]
        backtraking(j+1, total) # 더 한거 뒤에 있는 애들 더해서 확인
        total -= arr[j] # 아닌 애들 다시 빼줌

n, s = map(int, input().split())
arr = list(map(int, input().split()))
# visited를 이용한 백트래킹은 시간이 오래걸림
# visited = [0] * n
# 수열이라 앞에 있는 애들은 고려 안 해줄거라 visited 필요 X

cnt = 0
backtraking(0, 0)
print(cnt)
