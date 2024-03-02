from collections import deque
# 남학생(1) -> 스위치 번호의 배수를 다 바꿈
# 여학생(2) -> 스위치 번호 기준 대칭으로 같은지 검사 후 바꿈
def click(gen, n, lst):     # gender, number, list
    if gen == 1 :   # 남학생이면
        w = n
        while w <= len(lst):
            lst[w-1] = abs(lst[w-1]-1)
            w += n
    else :
        i = 0
        n -= 1
        while 0 <= n-i < len(lst) and 0 <= n+i < len(lst) :
            if lst[n-i] == lst[n+i]:
                lst[n-i] = lst[n+i] = abs(lst[n+i]-1)
                i +=1
            else :
                break


length = int(input())
# 정보) 스위치 번호는 1번부터 시작한다.
switch = deque(map(int,input().split()))

t = int(input())

for _ in range(t):
    gender, num = map(int,input().split())
    click(gender, num, switch)

count = 0
while switch :                          # 출력 부분
    count += 1
    print(switch.popleft(), end=" ")
    if count == 20 and switch :
        print()
        count = 0