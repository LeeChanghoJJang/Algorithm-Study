a, summary = map(int,input().split())       # a개의 정수와 목표 정수값을 받음

test_case = list(map(int,input().split()))  # 테케를 받고

count = 0                                   # 카운트를 설정

subset = [[]]                               # 부분집합 시작
for x in test_case :                        #
    size = len(subset)                      #
    for y in range(size) :                  #
        subset.append(subset[y] + [x])      # 비트 연산 없이 부분집합 만들기 

for i in subset :                           # 모든 부분집합의 리스트 중에서
    if sum(i) == summary and len(i) >= 1 :  # 길이가 1 이상이고, 합이 summary와 같다면
        count += 1                          # 카운트 +=1 
print(count)                                # 출력