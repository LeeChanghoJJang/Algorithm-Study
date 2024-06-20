import sys
sys.stdin = open('input.txt')
# 순열을 위한 백트래킹 정의
def backtracking(start, result):
    if len(result) == M:
        # copy를 하지 않으면 result가 바뀔 때마다 계속 갱신됨
        # 그 때의 result를 저장하고 싶어서임 
        temp.add(tuple(result.copy()))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result.append(arr[i])
            backtracking(start + 1, result)
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [0] * (N + 1)
# temp에 순열을 전부 저장
temp = set()
backtracking(0, [])
# 순서대로 뽑기
for i in sorted(temp):
    print(*i)
