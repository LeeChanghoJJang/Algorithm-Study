# 2836 수상 택시
# 주어진 L리스트 초기화
L = []

N, M = map(int, input().split())

for _ in range(N):
    s, e = map(int, input().split())
    if s > e: L.append([e, s])
    else: L.append([s, e])

# 구간을 끝점 기준으로 내림차순 정렬
L.sort(key=lambda x: -x[1])

# 병합된 구간을 저장할 리스트 초기화
tmp = []

# 첫 번째 구간을 시작 구간으로 설정
ts, te = L[0]

# 구간을 순회하며 병합
for i in range(1, len(L)):
    s, e = L[i]
    
    if ts <= e:  # 현재 구간이 이전 구간과 겹치는 경우
        ts = min(ts, s)
    else:  # 현재 구간이 이전 구간과 겹치지 않는 경우
        tmp.append([ts, te])
        ts, te = s, e

# 마지막 구간을 tmp에 추가
tmp.append([ts, te])

# 초기 길이에 모든 구간의 길이를 2배하여 더함
answer = M
for i in range(len(tmp)):
    answer += 2 * (tmp[i][1] - tmp[i][0])

print(answer)
