def div_conq(a,b,c):
    if b == 1 :
        return a % c
    
    if b % 2 == 1:
        return div_conq(a,b//2,c)**2 * a % c
    
    else :
        return div_conq(a,b//2,c)**2 % c
#### 재귀함수를 통해 10 ** 11 % 12를
    # (((10^2)*10)^2*10)% 12 로 만듬

A,B,C = map(int,input().split())

print(div_conq(A,B,C))