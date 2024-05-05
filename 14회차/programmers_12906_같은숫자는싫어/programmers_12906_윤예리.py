from collections import deque


def solution(arr):
    num_list = deque(arr)
    result = [-1]

    for _ in range(len(arr)):
        a = num_list.popleft()
        if a != result[-1]:
            result.append(a)

    return result[1:]