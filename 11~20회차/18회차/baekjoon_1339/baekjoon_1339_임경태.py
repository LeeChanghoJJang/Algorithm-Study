# 1339 단어 수학
from collections import defaultdict

N = int(input())
words = [input() for _ in range(N)]

# 알파벳 가중치를 저장할 딕셔너리
weight = defaultdict(int)

# 각 단어에 대해 가중치를 계산
for word in words:
    for i in range(len(word)):
        char = word[i]
        weight[char] += 10 ** (len(word)-i-1)

# 가중치가 큰 순서대로 정렬
sorted_weight = sorted(weight.items(), key=lambda x: -x[1])

# 숫자를 할당하기 위한 딕셔너리
char_to_num = {}
temp_num = 9

# 가중치가 큰 알파벳부터 숫자를 할당
for char, _ in sorted_weight:
    char_to_num[char] = temp_num
    temp_num -= 1

# 단어들의 합을 계산
ans = 0
for word in words:
    num = 0
    for char in word:
        num = num * 10 + char_to_num[char]
    ans += num

print(ans)

'''

문제의 본질 파악:
목표 : 각 단어의 알파벳에 숫자를 할당하여 단어들의 합을 최대화하는 것
이를 위해 각 알파벳에 적절한 숫자를 할당해야 하며, 자릿수가 높은 알파벳이 더 큰 가치를 갖는다.

최적 부분 구조 (Optimal Substructure):
그리디 알고리즘이 적용될 수 있는 문제는 보통 최적 부분 구조를 갖는다.
각 알파벳에 가장 큰 숫자를 할당하여 부분 문제를 최적화하면, 전체 합도 최적화

탐욕적 선택 속성 (Greedy Choice Property):
그리디 알고리즘은 각 단계에서 가장 최선의 선택을 하는 방식
이 문제에서 각 알파벳에 가장 큰 숫자를 할당하는 것이 가장 좋은 선택이다.
자릿수가 큰 알파벳부터 가장 큰 숫자를 할당하면 전체 합이 최대가 된다.

문제의 구조:
각 단어에서 자릿수마다 알파벳의 가중치를 계산하여 큰 가중치부터 큰 숫자를 할당하면 된다.
이는 단계별로 가장 큰 값을 선택하는 그리디 알고리즘의 특성과 일치함
'''