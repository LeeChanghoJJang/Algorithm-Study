N,K = map(int,input().split())
doll = list(map(int,input().split()))

# 투포인터
left = right = cnt = 0
# 초기값 설정
if doll[0] == 1:
    cnt += 1
 
ans = float('inf')

# 오른쪽으로 가는 경우 : 인형 수가 부족한 경우
# 왼쪽으로 가는 경우 : 인형 수가 충분한 경우 (이 경우 최소값 갱신)
while right < N :
    if cnt < K :
        right += 1
        if right < N and doll[right] == 1 :
            cnt += 1
    else :
        ans = min(right-left+1, ans)
        if doll[left] == 1:
            cnt -= 1
        left += 1

# 최소값이 갱신되지 않은 경우 -1
print(-1 if ans == float('inf') else ans)