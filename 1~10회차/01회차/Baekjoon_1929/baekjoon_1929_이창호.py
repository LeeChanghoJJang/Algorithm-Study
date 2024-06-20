# 1929번 소수구하기 
M,N = map(int,input().split())
# 1차시도 : 시간초과 
for num in range(M,N+1):
    cnt=0
    for divide in range(1,int(num**0.5)+1):
        if num % divide ==0:
            cnt+=1
    if cnt==1:
        print(num)

# 2차시도 : 성공 (31120KB 5320ms)
if M==1:
    M=2
for num in range(M,N+1):
    for divide in range(2,int(num**0.5)+1):
        if num % divide ==0:
            break
    else:
        print(num)
# 3차시도 : 에라토스 테네스의 체 (39368KB 580ms)
# 모든 수가 소수(True)인 것으로 초기화 
Eratos = [True for i in range(N + 1)] 
# 2부터 n의 제곱근까지
for num in range(2, int(N**0.5) + 1): 
    if Eratos[num]: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while num * j <= N:
            Eratos[num * j] = False
            j += 1

# 모든 소수 출력
for num in range(M, N + 1):
    if Eratos[num]:
        if num != 1:
            print(num)
'''
개선점
두번째 시도 시, 이전과 다른 점이라 하면 for-else 구문과 break를 활용했다는 점이다
하지만, 세번째 에라토스 테네스의 체는 메모리가 조금 많이 들지만, 뒤에 순회해야 할 대상들도
일부 소수판별을 미리 하기 때문에 시간이 많이 절약됨.
'''