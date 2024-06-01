# 입력
N,M = map(int,input().split())
arr = [*map(int,input().split())]

# left는 약속으로 해소할 수 없는 남는 날짜
left = M - N - sum(arr)
# 항상 일이 있으면 그냥 0
if left <= 0: exit(print(0))

# 아니라면 적절히 분배해야함
# 2 2 2 2 3 3 이런식으로 최대한 평탄화해서 담아야하기 때문에
# k : left를 N+1개의 칸에 각각 나누고
# l : 남은 숫자도 따로 저장
k = left // (N+1)
l = left % (N+1)

# tmp는 각 
tmp = 0
for i in range(k+1):
	tmp += i**2

# 해를 계산
# (N+1) * visit[k] : k까지 더한 제곱수 N+1개
# 나머지 l 개만큼 (k+1)**2를 또 더해줌
ans = (N+1)*tmp + (k+1)**2 * l

# 출력
print(ans)