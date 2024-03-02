import sys
sys.stdin = open('input.txt')

h = sorted(int(input()) for _ in range(9))
s = sum(h)

for i in range(8):
    for j in range(i+1, 9):
        if s - h[i] - h[j] == 100:
            for k in h:
                if k != h[i] and k != h[j]:
                    print(k)
            exit()

'''
31120KB / 44ms
'''