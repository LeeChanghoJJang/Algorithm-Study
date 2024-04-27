import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    count = 0
    for num in str(tc+1):
        if num == '3' or num == '6' or num == '9': count += 1
    if count == 0: print(tc+1, end=' ')
    else: print('-' * count, end=' ')
