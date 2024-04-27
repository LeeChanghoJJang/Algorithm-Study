import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [str(i) for i in range(1, n+1)]
clap = ['3', '6', '9']

for i in range(n):  # arr 순회하면서 -으로 바꿈
    arr[i] = arr[i].replace('3', '-')
    arr[i] = arr[i].replace('6', '-')
    arr[i] = arr[i].replace('9', '-')

for j in range(n):
    if arr[j].isdigit():
        pass
    elif arr[j] == '-':
        pass
    elif arr[j] == '--':
        pass
    elif arr[j] == '---':
        pass
    else:
        arr[j] = '-'

print(*arr)