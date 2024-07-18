from collections import deque

N,A,B = map(int,input().split())
res = deque()
# A가 무조건 같거나, 더 크다고 가정
if A>=B: check = 1
# 아닌 경우 뒤집고 뒤집었다 표시(check)
else: 
    check = 0
    A,B = B,A

# A부터 순회하면서 1 2 3 순서대로 구성
for a in range(1,A+1):
    res.append(a)
# 반대로 B는 역순으로 구성
for b in range(B-1,0,-1):
    res.append(b)

# 이렇게 구성했을 때 이미 배열보다 많다면 -1
if N < len(res):
    exit(print(-1))

# 남은건 1로 채움
# 예시
# 10 4 1
# 1 1 1 1 1 1 1 2 3 4
if check :
    while N > len(res):
        res.appendleft(1)

# 예시
# 10 1 4
# 4 1 1 1 1 1 1 3 2 1 
# 1번 인덱스에 채워야 맞음
else:
    res.reverse()
    while N > len(res):
        res.insert(1,1)
# 출력
print(*res)