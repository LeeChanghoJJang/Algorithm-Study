T = int(input())

# 16개의 MBTI 중
# 33명 이상이라면 같은 MBTI인 3명이 최소 한 쌍 존재한다.

for _ in range(T):
    N = int(input())
    MBTI = input().split()

    if N > 32 : 
        print(0)
        continue
    ans = float('inf')
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                cnt = 0 
                for idx in range(4):
                    if MBTI[i][idx] != MBTI[j][idx] :
                        cnt += 1
                    if MBTI[i][idx] != MBTI[k][idx] :
                        cnt += 1
                    if MBTI[j][idx] != MBTI[k][idx] :
                        cnt += 1
                ans = min(ans,cnt)
    print(ans)