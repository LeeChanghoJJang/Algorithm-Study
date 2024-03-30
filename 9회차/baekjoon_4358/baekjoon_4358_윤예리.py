woods = {}
num = 0
while True:
    try:
        w = input()

        num += 1
        try:
            woods[w] += 1
        except:
            woods[w] = 1
    except:
        break 

for i in sorted(woods.keys()):
    print(f'{i} {woods[i]/num*100:.4f}')