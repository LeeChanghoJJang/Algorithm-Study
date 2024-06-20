# 백준 10815번 숫자카드 
import sys
N = int(sys.stdin.readline()) # 상근이가 갖고 있는 숫자카드 개수
cards = sorted(list(map(int,sys.stdin.readline().split()))) # 상근이가 갖고 있는 숫자카드 
# 상근이가 들고 있는지 여부를 판단할 숫자의 리스트의 개수
M = int(sys.stdin.readline())
# 상근이가 들고 있는지 여부를 판단해야할 숫자의 리스트 
checks = list(map(int,sys.stdin.readline().split()))
# checks에 있는 숫자의 리스트 각각이 상근이가 들고 잇는지 여부를 담을 결과 리스트  
result = []
# checks 반복문 순회 
for check in checks:
  start = 0 # 초기값 설정(시작)
  end = N-1 # 초기값 설정(끝)
  while start <=end: # 시작보다 끝이 작은 경우 while문 반복하여 계속 탐색
    mid = (start+end)//2 # 이진 탐색방법에 따라 중간값 지정 
    if check < cards[mid] : # 카드의 중앙에 위치한 값이 checks의 값보다 큰 경우
      end = mid-1 # end를 mid값보다 작게 조정 
    elif check > cards[mid] :
      start= mid +1
    else:
      result.append(1) # 상근이가 들고있는 카드가 확인해야할 카드가 checks에 있는 경우 1 추가
      break
  else:
    result.append(0) # while문을 다 순회했음에도 값이 없으면 0 결과 리스트에 추가 
print(*result) # 결과값 모은 리스트를 언팩