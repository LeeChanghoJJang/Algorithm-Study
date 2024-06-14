N = int(input())

alphabet = [input() for _ in range(N)]

position = [[] for _ in range(8)]
for idx in range(7,-1,-1) :
    for char in alphabet:
        if len(char) > idx :
            position[idx].append(char[-idx-1])

counter = {}
for i in range(7,-1,-1):
    for alpha in position[i]:
        counter[alpha] = counter.get(alpha,0)+10**i
        
num = 9
ans = 0
for i in sorted(list(counter.values()), reverse=True):
    ans += num * i
    num -= 1
   
print(ans)