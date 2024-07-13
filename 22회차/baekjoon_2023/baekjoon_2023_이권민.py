f_lst = [2,3,5,7]
lst = [1,3,7,9]
def checkPrimeNum(check_number):
    #에라토스테네스의 체로 소수인지 확인
    for i in range(2, int(check_number**0.5)+1): 
        if int(check_number) % i == 0: 
            return False
    return True

N = int(input())

def dfs(cur,num):
    if cur == N:
        print(num)
        return 
    for i in range(4):
        if checkPrimeNum(int(num + str(lst[i]))):
            dfs(cur+1, num + str(lst[i]))
for num in f_lst:
    dfs(1, str(num))
        