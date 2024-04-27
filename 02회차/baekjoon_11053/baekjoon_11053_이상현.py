# 백준 11053번 가장 긴 증가하는 부분 수열
import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = list(map(int, input().split()))

# dp를 이용한 풀이
# 수열을 이루는 수의 최댓값이 1000이므로 길이가 1001인 max_seq를 선언
max_seq = [0] * 1001

for num in num_list:
    # max_seq[num]은 num 숫자를 마지막으로 가지는 수열 중 가장 긴
    # 증가하는 부분 수열의 길이와 같음
    max_seq[num] = max(max_seq[:num]) + 1
print(max(max_seq))