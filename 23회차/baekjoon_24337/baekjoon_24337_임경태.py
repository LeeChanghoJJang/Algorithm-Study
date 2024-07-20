# 24337 가희와 탑
N, A, B = map(int, input().split())
ans = []

# 왼쪽 부분 채우기
for i in range(1, A):
    ans.append(i)

# 최고값 추가
ans.append(max(A, B))

# 오른쪽 부분 채우기
for i in range(B-1, 0, -1):
    ans.append(i)

 # 조건이 만족이 안되는 경우
if len(ans) > N:
    print(-1)
else:
    print(ans[0], end=" ")

    for i in range(N-len(ans)):
        print(1, end=" ")

    for i in range(1, len(ans)):
        print(ans[i], end=" ")