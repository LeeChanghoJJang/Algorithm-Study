## Algorithm Study 1회차 회의 (24.2.3.)

### 🪙 회의개요
    가. 금일 일정 
        - 시간 : 2월 3일 토요일 10시
        - 장소 : 스타벅스 김해 율하 신도시점

    나. 차주 예정 일정
        - 시간 : 2월 12일 월요일 9시 30분
        - 장소 : 커피팀버 김해장유점 

### 🎵 문제 선정 및 방식 
    가. 유형 : 『유형』 별로 문제 선정 
    나. 문제수 : 인당 3문제, 총 12문제
    다. 난이도 : 백준 실버 상위 난이도 위주
    라. 그 외 : 스터디원들이 풀지 않았던 문제 위주 선정
    마. 코드 브리핑 && 리뷰 방식
      - 문제 선정자가 푼 방식 브리핑
      - 푼 방식 이외에도 다양한 방법 제시
      - 문제 접근 방식 우선순위 등 총체적 정리
###### 1. 예리 
    - 19189 순열의 아름다움 - swea
    - 1868 파핑파핑 숫자찾기 - swea
    - 11053 가장 긴 증가하는 부분수열 - 백준 
    - 1783 병든 나이트 - 백준
###### 2. 상현
    - 11660 구간합 구하기 5 - 백준
    - 17276 배열 돌리기 - 백준
    - 2630 색종이 만들기 = 백준
###### 3. 창호
    - 2806 N-Queen - swea
    - 8822 홀수-값 피라미드 1 - swea
    - 14888 연산자 끼워넣기 - 백준
###### 4. 경태
    - 1343 폴리오미노 - 백준
    - 3986 좋은단어 - 백준
    - 12173 금화 모으기 - swea
      
### 🏅 스터디 내용 
#### 🎈 백준 10815 숫자카드
> 이진탐색(3172ms) : 이진탐색 함수 정의하여 반복문 순회횟수 감소
```python
# 이진 탐색 구현
# 1단계 : 정렬된 배열에서 목표수를 찾기 위한 반복문 순회
import sys
cards = sorted(list(map(int,sys.stdin.readline().split())))
checks = list(map(int,sys.stdin.readline().split()))
result = []
for check in checks:
  # 2단계 : 초기값 설정(시작과 끝)
  start = 0 
  end = N-1 
  # 3단계 시작보다 끝이 작은 경우 반씩 범위를 줄여서 반복
  while start <=end:
    mid = (start+end)//2 # 반씩 범위를 줄이기 위해 mid 설정 
    if check < cards[mid]: # mid값이 목표수보다 큰 경우
      end = mid-1 # end를 mid값보다 작게 조정 
    elif check > cards[mid]: # mid값이 목표수보다 작은 경우 
      start= mid +1 # start를 mid값보다 작게 조정 
    # 4단계 목표 수를 찾은 경우 result에 1추가
    else:
      result.append(1) 
      break
  # 5단계 : 목표 수를 못찾은 경우 result에 0추가
  else:
    result.append(0)
```
> 입력방식 : Set, Dict(자료형) 주로 이용
```python
# Set : 중복되지 않아도 상관없는 num_list를 set으로 변경
num_list = set(map(int, input().split()))
target_num = list(map(int, input().split()))

for num in target_num:
    if num in num_list:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
# Dictionary : 고유값으로 딕셔너리의 키는 활용 쉬움 
M_card = {}
for i in list(map(int, sys.stdin.readline().split())):
    M_card[i] = 0
# 상근이가 가지고 있는 카드 순회
for num in N_card:
    # 카드가 딕셔너리의 키 목록에 있으면 1로 변경
    if num in M_card.keys():
        M_card[num] = 1
'''
참고로, M-card[num] +=1 하는 방식으로 기존 값에 더하는 건 안통함
'''
```
    

#### ⚽ 백준 11399 ATM
> 입력방식 : sorted 뒤에 list 자료형 변환 필요 없음
       
```python
# 입력받을 때 : sorted 뒤에 list가 아닌 map, filter가 와도 list화가 이뤄짐
# 입력 : 1 9 7 7 5
arr = sorted(map(int,input().split()))
arr = sorted(list(map(int,input().split())))
print(arr)
# 출력 : [1, 5, 7, 7, 9]
```
> 누적합 구하는 방식 2가지
> - 정렬된 배열에서 앞자리의 수를 더하는 반복문 순회
> - 정렬된 배열에서 각 수에 인덱스+1만큼 곱하는 반복문 순회

```python
# 누적합 구하는 방식
# 첫번째 : 카운트정렬처럼 앞의 수를 누적 합산한 배열에 Sum적용
arr = [1,3,4 ,6,8,11]  # 정렬된 배열이어야 함
for i in range(len(arr)-1):
    arr[i] += arr[i-1]
print(sum(arr))
# 두번째 : 애초부터 반복문 순회할 때마다 인덱스를 곱한 배열의 수 합산
arr = [1,3,4,6,8,11]
min_value = 0
for i in range(len(arr)):
    min_value += arr[i] * (i+1)   
print(min_value)
# 출력 : 149
```    

#### 🎄백준 1476 날짜계산
> 주요 방법 : while문 통해서 (year - 몫) !=0인 경우를 출력
```python 
# E : 지구, S : 태양, M : 달
# E는 15를, S는 28을, M은 19를 나눈 나머지
# 즉, 현재 나머지를 빼고서 각 15,28,19를 나누었을 때 0이 되는 수가 찾고자 하는 목표수
E,S,M = map(int,input().split())
year = 1 # 문제에서 1부터 주어졌으며, 1부터 해야 7,980 끝 수 출력가능
while 1: 
    if (year-E) % 15 == 0 and (year-S)%28 ==0 and (year-M)%19==0:
        break
    year+=1
print(year)
```
#### 🎀 백준 1929 소수 구하기
> 에라토스 테네스의 체 적극 활용
```python
M, N = map(int, input().split())
# 소수를 '체'에 거르기 위해 소수이면 1, 아니면 0으로 남을 배열 
prime = [0, 0, 1] + [1] * (N - 2)

# 소수이면 1, 소수가 아니면 0인 배열
for num in range(2, int(N**0.5) +1):
    if prime[num]:
        # 에라토스테네스의 체 사용
        # 소수의 배수는 전부 합성수이므로 0으로 처리
        for index in range(2 * num, N + 1, num):
            prime[index] = 0

for i in range(M, N+1):  # 범위 내에서 출력
    if prime[i]:
        print(i)
# 위 코드의 시간 복잡도는 O(N * log(log N))
```
#### 🥋 문제 외
> 얕은복사, copy, 깊은 복사(deepcopy) 차이 이해 
```python    
import copy
arr=[[1,2,3],[4,5,6],[7,8,9]] # 원본
arr1 = copy.deepcopy(arr) # 깊은복사 : 원본값 수정해도 안바뀜 
arr2 = arr.copy() # 메모리 주소만 참조 --> 원본값이 변하면 바뀜
arr3 = arr[:] # 얕은 복사 : 1차원 행렬까지만 원본값 수정시 안바뀜
print(arr1,arr2,arr3)
# 출력
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr[0][0]=10
print(arr1,arr2,arr3)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [[10, 2, 3], [4, 5, 6], [7, 8, 9]] [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
```
