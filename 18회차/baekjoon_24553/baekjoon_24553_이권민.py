
# 1의 자리는 모두 펠린드롬 수. 내차례에 팰린드롬 수를 만들면 안됨.
# 10의 배수일때 1. 10의 배수가 아니면 1빠가 10의 배수를 만들어서 이김_0
# DP구나. 라고했지만 N이 10**18
'''
DP = [0 for _ in range(101)]
DP[0] = 1
palin = []
def is_palin(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True
for i in range(1, 101):
    if is_palin(str(i)):
        palin.append(i)

for i in range(1, 101):
    for p in palin:
        if i-p >= 0 and DP[i-p] == 1:
            break
    else:
        DP[i] = 1
'''

import sys
input = sys.stdin.readline
T = int(input())
# 팰린드롬이면 0. 아니면 뺏을때 상대승이 아닌 게 있으면.

for _ in range(T):
    print(int(not bool(int(input())%10)))    

    