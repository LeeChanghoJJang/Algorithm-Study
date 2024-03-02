N = int(input())
 
for num in range(1, N + 1):
    cnt = 0
    cnt = sum(i in '369' for i in str(num))
    print('-' * cnt if cnt else num, end = ' ')