# MITM가 뭔데요..?

# Meet In The Middel, 중간에서 만나기
# 리스트 이분화 > 조합 > 정렬 > 이분탐색의 과정을 거친다. 

from itertools import combinations

N,C = map(int,input().split())

bags = list(map(int,input().split()))
# 1. 가방을 반으로 쪼갠다
bag1 = bags[:N//2]
bag2 = bags[N//2:]

tmp1 = []
tmp2 = []
# 2. 각자 combinations을 구해서 그 합을 임시 리스트에 담는다.
for i in range(len(bag1)+1):
    comb1 = combinations(bag1,i)

    for comb in comb1 :
        # print(comb)
        tmp1.append(sum(comb))
        
for i in range(len(bag2)+1):
    comb2 = combinations(bag2,i)

    for comb in comb2 :
        # print(comb)
        tmp2.append(sum(comb))

# print(tmp1)
# print(tmp2)

# 3. 한 리스트를 정렬하고
tmp1.sort()
ans = 0 
# 나머지 리스트를 순회하면서 
for a in tmp2 :
    # C보다 커지면 넘어가고,
    if a > C :
        continue
    # 4. 그 이외의 경우에서 이분탐색을 진행한다. 
    start = 0
    end = len(tmp1)-1

    while start <= end :
        mid = (start+end) // 2

        if tmp1[mid] + a > C :
            end = mid-1
        else :
            start = mid+1
    # 이분 탐색이 완료된 경우 end +1 값을 ans에 더해준다.
    ans += end + 1

print(ans)