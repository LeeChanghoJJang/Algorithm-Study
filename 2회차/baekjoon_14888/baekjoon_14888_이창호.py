from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
arr =  list(map(int,input().split()))
operators = list(map(int,input().split()))
min_val = 1e9
max_val = -1e9

def dfs(n,temp):
    global min_val,max_val

    # n이 0부터 증가하여 N-1이 되는경우
    # 왜냐하면 맨첨에 연산은 숫자 두개가 필요한데 옆에 최초숫자넣을거임
    if n ==N-1:
        min_val = min(temp,min_val)
        max_val = max(temp,max_val)
        return

    # 각 연산자별 연산결과 도출
    if operators[0] != 0 : # 덧셈하는 경우
        operators[0] -=1
        dfs(n+1,temp + arr[n+1])
        operators[0] +=1

    if operators[1] != 0 : # 빼는 경우
        operators[1] -=1
        dfs(n+1,temp - arr[n+1])
        operators[1] +=1

    if operators[2] != 0 : # 곱하는 경우
        operators[2] -=1
        dfs(n+1,temp * arr[n+1])
        operators[2] +=1

    if operators[3] != 0 : # 나눗셈하는 경우
        operators[3] -=1
        dfs(n+1,int(temp / arr[n+1]))
        operators[3] +=1

dfs(0,arr[0])
print(max_val)
print(min_val)
