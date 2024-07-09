# 오름차순으로 소수인지 확인하면서 백트래킹
def isprime(number):
    if number < 2: return False
    for i in range(2,int(number**0.5)+1):
        if not number % i: return False
    return True

def backtrack(idx, result=0) :
    if idx==0: return print(result)
    for i in range(1,10):
        if isprime(result*10 + i): backtrack(idx-1, result*10+i)

backtrack(int(input()))