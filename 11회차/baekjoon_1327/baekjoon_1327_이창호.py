import sys
sys.stdin = open('input.txt')  # 표준 입력을 'input.txt' 파일에서 읽도록 설정
from collections import deque

def bfs(initial, target):
    n = len(initial)
    visited = set()  # 방문한 상태를 저장할 집합
    queue = deque([(initial, 0)])  # 초기 상태와 카운트 0을 갖는 큐를 생성

    while queue:
        current,  count = queue.popleft()  # 현재 상태와 카운트를 큐에서 추출

        if current == target:  # 현재 상태가 목표 상태와 같으면
            return count  # 연산 횟수를 반환

        if tuple(current) not in visited:  # 현재 상태가 방문되지 않았다면
            visited.add(tuple(current))  # 현재 상태를 방문한 것으로 표시
            for i in range(n - k + 1):  # 연속된 k개의 요소를 뒤집을 수 있는 가능한 위치를 반복
                # 인덱스 i에서 연속된 k개의 요소를 뒤집고 큐에 추가
                new_board = current[:i] + list(reversed(current[i:i + k])) + current[i + k:]
                queue.append((new_board, count + 1))  # 새로운 상태와 카운트를 큐에 추가하고 카운트를 증가

    return -1  # 목표 상태에 도달할 수 없으면 -1을 반환

# 입력값을 읽음: n은 요소의 개수, k는 부분 시퀀스의 크기
n, k = map(int, input().split())
# 초기 상태를 정수 리스트로 읽음
initial_state = list(map(int, input().split()))
# 초기 상태를 정렬하여 목표 상태를 얻음
target_state = sorted(initial_state)

# 초기 상태와 목표 상태를 이용하여 BFS 함수를 호출하고 결과를 출력
result = bfs(initial_state, target_state)
print(result)
