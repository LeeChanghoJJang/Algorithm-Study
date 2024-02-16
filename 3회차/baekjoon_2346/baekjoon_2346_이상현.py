# 백준 2346번 풍선 터뜨리기

from collections import deque

# 덱을 이용하여 접근
# 풍선의 번호를 출력해줘야 하기 때문에 enumerate를 이용하여
# 풍선의 번호를 풍선에 적힌 번호와 함께 저장
N = int(input())
num_list = deque(enumerate(map(int, input().split()), start = 1))
result = []

# 터뜨려야할 풍선을 맨 앞에 위치하게 리스트를 회전시킴
while num_list:
    # index는 터진 풍선의 번호를, num은 터진 풍선에 적힌 수를 의미
    index, num = num_list.popleft()
    result.append(index)

    # 파이썬 deque 라이브러리의 rotate(n)메서드는 덱의 요소들을
    # 오른쪽으로 n만큼 회전시킴 (n이 음수면 반대)

    # 풍선에 적힌 숫자가 양수라면, 리스트를 왼쪽으로 회전시켜줘야함
    # 음수라면 오른쪽으로 회전시켜줘야함
    if num > 0:
        num_list.rotate(1 - num)
    else:
        num_list.rotate(-num)

print(*result)