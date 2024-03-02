# 2309 일곱 난쟁이

height = sorted(int(input()) for _ in range(9))
s = sum(height)

for i in range(8):
    for j in range(i+1, 9):
        if s - height[i] - height[j] == 100:
            for h in height:
                if h != height[i] and h != height[j]:
                    print(h)
            exit()

'''
31120KB / 44ms
'''