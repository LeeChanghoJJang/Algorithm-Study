import sys
sys.stdin = open('input.txt')
input=sys.stdin.readline
N = int(input().strip())
nums = {}
max_len = 0
for i in range(N):
    word = list(input().strip())
    for idx,j in enumerate(word,1):
        if nums.get(j):nums[j] += 10**(len(word)-idx)
        else: nums[j] = 10**(len(word)-idx)
nums_dict= {}
start = 9

for i in sorted(nums.keys(),key=lambda x:-nums[x]):
    nums_dict[i] = start
    start-=1

print(sum(map(lambda x:nums_dict[x]*nums[x],nums_dict.keys())))