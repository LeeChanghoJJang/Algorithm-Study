from collections import deque

N,K = map(int,input().split())
arr = tuple(map(int,input().split()))
target = tuple(sorted(arr))

ans = -1
q = deque([(arr,0)])

# visit를 dict로 받아서 해싱으로 방문 처리하기
visit = dict()

while q : 
    arr, cnt = q.popleft()

    if arr == target :
        ans = cnt 
        break
    
    for i in range(N-K+1) :
        # 딕셔너리 key에 list를 넣을 수 없어 tuple로 처리
        rev = arr[:i] + tuple(reversed(arr[i:i+K])) + arr[i+K:]
        
        # 딕셔너리에 없으면
        if not visit.get(rev) :
            # 키값 하나 생성해서 방문 처리하고 
            visit[rev] = True
            # 뒤집은거 리스트로 다시 바꾸고 카운트올려서 q에 더함
            q.append((rev,cnt+1))

print(ans)
# 리스트 + 방문처리 1 vs True 37520kb ,  460ms / 436ms
# 튜플로 계산시 38984kb , 348ms