N, M= int(input()), int(input())
S = input()

ans, idx, cnt = 0,0,0           # ans : 총 값 idx : 인덱스 cnt : 카운트 (cnt == N > IOIOI)

while idx < M-1:
    if S[idx:idx+3] == "IOI":   # IOI를 같이 보면 시간 3배 절약
        idx += 2                # 인덱스는 2칸씩 전진
        cnt += 1                # cnt 1 증가

        if cnt == N :           # 카운트가 N까지 올라간 경우
            ans +=1             # ans 올리고
            cnt -=1             # cnt 한칸 내려서 다음에 또 cnt 올리면 바로 ans 올리게 만들기
    else :                      # IOI가 안나오면
        idx += 1                # idx 한칸만 올리고
        cnt = 0                 # cnt 0 으로 초기화

print(ans)                      # 출력