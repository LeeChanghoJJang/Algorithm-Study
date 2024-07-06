import sys
sys.stdin  = open('input.txt')

def back(k,result,j):
    global min_str
    global max_str
    if j==k or len(result) == k+1:
        if min_str > result:
            min_str = result
        if max_str < result:
            max_str = result
        return

    for i in range(10):
        if not visited[i] and (not result or result and eval(f'{result[-1]} {equals[j]} {i}')):
            visited[i] = 1
            if result:
                back(k, result + str(i), j + 1)
            else:
                back(k, result + str(i), j)
            visited[i] = 0

k = int(input())
equals = input().split()
min_str = '9999999999'
max_str = ''
visited = [0] * 10
back(k,'',0)
print(max_str)
print(min_str)