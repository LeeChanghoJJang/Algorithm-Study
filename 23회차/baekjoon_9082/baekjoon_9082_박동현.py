# 백트래킹 돌리면 길이 25만 되도 26초 걸림
# 무조건 가능한 모양만 만들어주기 때문에 주어지는 지뢰는 볼 필요도 없음

for _ in range(int(input())):
    N = int(input())
    cnt = [-1]+[*map(int,list(input()))]+[-1]
    input()
    
    ans = 0
    for i in range(1,N+1):
        if cnt[i-1] and cnt[i] and cnt[i+1]:
            for x in -1,0,1:
                cnt[i+x] -= 1
            ans += 1
    print(ans)