# baekjoon_1343 폴라오미노
A = input()
A = A.replace('XXXX','AAAA').replace('XX','BB')
if 'X' in A:
    print(-1)
else:
    print(A)
