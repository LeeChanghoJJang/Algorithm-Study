import sys
sys.stdin = open('input.txt')

N = int(input())
weights = sorted(map(int,input().split()))
target = 1

for weight in weights:
    # 만약 현재 추의 무게가 target 이하라면 target을 업데이트
    if weight <= target:
        target += weight
    else:
        break
print(target)