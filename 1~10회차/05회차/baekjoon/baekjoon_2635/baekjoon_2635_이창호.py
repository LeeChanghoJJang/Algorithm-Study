import sys
sys.stdin =open('input.txt')
N = int(input())
# search 함수는 두 수가 주어질 때, 이어가는 수열을 반환하는 함수
def search(num,N):
    temp = [N,num]
    while N:
        if N-num < 0:
           break
        temp.append(N - num)
        N, num = num, N-num
    return temp

max_val = 0
result = []
# N보다 작은 수에 대해 모두 search 함수 돌리기 
for i in range(N+1):
    if max_val < len(search(i,N)):
        max_val = len(search(i,N))
        result = search(i,N)
print(max_val)
print(*result)

