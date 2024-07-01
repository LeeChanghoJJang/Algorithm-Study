# 두 큐 합 같게 만들기

from collections import deque


def solution(queue1, queue2):
    left = sum(queue1)
    right = sum(queue2)
    leftQ = deque(queue1)
    rightQ = deque(queue2)

    limit = 2 * (len(queue1) + len(queue2))

    cnt = 0

    if (left + right) % 2 == 1:
        return -1

    while cnt < limit:

        if left == right:
            return cnt

        if left < right:
            gap = rightQ.popleft()
            left += gap
            right -= gap
            leftQ.append(gap)

        else:
            gap = leftQ.popleft()
            right += gap
            left -= gap
            rightQ.append(gap)

        cnt += 1
    return -1