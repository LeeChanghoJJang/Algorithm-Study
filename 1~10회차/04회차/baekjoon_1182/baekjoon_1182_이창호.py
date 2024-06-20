# 첫번째 방법 (31120KB , 336ms)
import sys
N,S = map(int,sys.stdin.readline().split())
integers = tuple(map(int,sys.stdin.readline().split()))
cnt=0
# 재귀함수 이용
def back(start,result):
    global cnt
    # 합이 S고, start가 0보다 크면(맨 처음이 포함되면 바로 cnt 1추가되는 경우 발생)
    # 부분집합의 개수 구하는 것과 동일하게 진행
    if result == S and start>0:
        cnt +=1
    # start부터 end까지 탐색하여, result값에 연산결과 저장
    for end in range(start,N):
        back(end+1,result+integers[end])

back(0,0)
print(cnt)

# 두번째 방법 (31120KB 3248ms)
import sys
N,S = map(int,sys.stdin.readline().split())
integers = tuple(map(int,sys.stdin.readline().split()))
cnt=0
# 부분집합의 모든 경우의수를 구함 ==> 결과가 S면 카운팅
for row in range(1,1<<N):
    result = 0
    for col in range(N):
        if row & (1<<col):
            result += integers[col]
    if result == S:
        cnt +=1
print(cnt)
