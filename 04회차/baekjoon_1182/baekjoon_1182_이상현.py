# 백준 1182번 부분수열의 합

# 주어진 수열의 부분 수열 중에서 합이 S가 되는
# 부분 수열의 개수를 구하는 문제
def dfs(idx, sum_):
    global cnt

    # 만약 부분수열의 크기가 양수이고 합이 S와 같다면 cnt를 1 증가시킴
    if idx and sum_ == S:
        cnt += 1

    # num_list[i]를 포함한 경우와 포함하지 않은
    # 경우 모두 탐색
    for i in range(idx, N):
        sum_ += num_list[i]
        dfs(i + 1, sum_)
        sum_ -= num_list[i]

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)