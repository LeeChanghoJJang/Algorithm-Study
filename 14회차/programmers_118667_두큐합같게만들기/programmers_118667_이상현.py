from collections import deque


def solution(queue1, queue2):
    left_sum = sum(queue1)
    right_sum = sum(queue2)
    sum_ = left_sum + right_sum
    len_ = len(queue1) + len(queue2)
    answer = 0

    if sum_ % 2 != 0:
        return -1

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while left_sum != right_sum and answer < 2 * len_ + 1:
        if left_sum > right_sum:
            temp = queue1.popleft()
            queue2.append(temp)
            left_sum -= temp
            right_sum += temp
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            right_sum -= temp
            left_sum += temp
        answer += 1

    if answer < 2 * len_ + 1:
        return answer
    return -1