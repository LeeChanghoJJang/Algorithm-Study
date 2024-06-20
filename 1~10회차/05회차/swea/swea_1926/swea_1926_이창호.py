import sys
sys.stdin = open('input.txt')

def judge(number):
    result=''
    if any(i in str(number) for i in ['3','6','9']):
        while number:
            k,v = divmod(number,10)
            if v%3 ==0 and v !=0:
                result+='-'
            number = k
        return result
    else:
        return number

N = int(input())
for i in range(1,N+1):
    if i == N:
        print(judge(i))
    else:
        print(judge(i),end=' ')