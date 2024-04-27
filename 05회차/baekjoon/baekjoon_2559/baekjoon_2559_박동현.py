T,K= map(int,input().split())

sums = 0

# 1,2 를 더하고 값을 저장함
# 저장된 값에서 3을 더하고 1을 뺌
temperature = list(map(int,input().split()))

rem = 0 
for idx in range(K): 
    rem += temperature[idx]

sums = rem

for idx in range(K, T):
    rem = rem - temperature[idx-K] + temperature[idx]
    if rem > sums:
        sums = rem

print(sums)
