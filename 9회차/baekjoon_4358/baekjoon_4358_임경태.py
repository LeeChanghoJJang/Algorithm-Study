# 4358 생태학
# 1. 입력시킨 나무를 개수와 같이 저장
# 2. 나무 전체 개수 합산
# 3. 나무 이름 오름차순 정렬
# 4. 출력

import sys
input = sys.stdin.readline

woods = {}
total_cnt = 0

while True:
        # input을 readline으로 받았으므로 마지막 문자는 '' 
        wood = input().rstrip()
        if wood == '': break

        if wood in woods:
            woods[wood] += 1
        else:
            woods[wood] = 1
        total_cnt += 1

for wood, cnt in sorted(woods.items()):
    print(f'{wood} {100*cnt/total_cnt:.4f}')

'''
<딕셔너리의 정렬>
1. sorted(dict.items()) : 딕셔너리의 아이템들이 튜플로 묶여 리스트에 정렬된다.
2. dict(sorted(dict.items())) : 정렬된 상태로 다시 딕셔너리에 저장된다.
3. sorted(dict) : 딕셔너리의 키만 따로 빠져 정렬된다.

<시간 복잡도>
1. while loop : O(n)
2. dict에 요소 추가 : O(1) / O(n) -> worst case
3. dict sort : O(nlogn)
'''