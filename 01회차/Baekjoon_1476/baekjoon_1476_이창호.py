# 1476번 날짜 계산
# 내 코드 31120KB 44ms
E,S,M = map(int,input().split())
# 지구 : E, 태양 : S, 달 : M
# count_arr로 입력한 E,S,M의 나머지가 일치한 경우 +1
count_arr =[0]*(15*28*19+1)
for answer in range(1,15*28*19+1):
    if answer % 15 == (E%15):
        count_arr[answer] +=1
    if answer % 28 == (S%28):
        count_arr[answer] += 1
    if answer % 19 == (M%19):
        count_arr[answer] += 1
    if count_arr[answer] ==3:
        print(answer)
        break

# 다른 이의 코드 31120KB 40ms
E,S,M = map(int,input().split())
# 지구 : E, 태양 : S, 달 : M
# count_arr로 입력한 E,S,M의 나머지가 일치한 경우 +1
year = 1
while 1:
    if (year-e) % 15 == 0 and (year-s)%28 ==0 and (year-m)%19==0:
        break
    year+=1
print(year)