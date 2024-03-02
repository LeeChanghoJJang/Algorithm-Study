import sys
sys.stdin = open('input.txt')

n = int(input())    # 학생 수
numbers = list(map(int, input().split()))   # 뽑은 수
result = []

for i in range(n):
    result.insert(i-numbers[i], i)
for i in range(n):
    print(result[i]+1, end=' ')