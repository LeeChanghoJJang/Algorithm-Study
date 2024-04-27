def calc(lst):                      # 계산기
    global ans                      # ans : 답 , 글로벌 설정
    while lst :                     # pop하면서 계산하므로 리스트가 빌때까지
        if len(lst) > 1:            # 리스트에 남은 값이 2개 이상이면
            a = lst.pop()           # 값을 두개 받아서
            b = lst.pop()
            if a==1 or b==1 :       # 둘다 1이면 더하고
                ans += a+b
            else :                  # 아니면 곱함
                ans += a*b
        else :                      # 리스트에 남은 값이 하나면
            a = lst.pop()
            ans += a                # 그냥 꺼내서 더하기
        
arr = [int(input()) for _ in range(int(input()))]
ans = 0

plus, minus= [], []
for i in arr :
    if i > 0 : plus.append(i)
    else: minus.append(i)
plus.sort()
minus.sort(reverse=True)            # 음수는 내림차순으로 정렬해서 절대값이 큰 값부터 곱해지게 설정

calc(plus); calc(minus); print(ans) # 함수 호출 후 출력