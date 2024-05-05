from collections import deque
def solution(queue1, queue2):
    # queue1 과 queue2
    queue1 = deque(queue1); queue2 = deque(queue2)
    q1_sum = sum(queue1);q2_sum = sum(queue2)
    n = len(queue1) + len(queue2)
    # 두 큐의 합이 홀수면 -1 반환
    if (q1_sum+ q2_sum) % 2: return -1
    count = 0
    # 반복 횟수가 총 길이의 2배면 중단
    while queue1 and queue2 and count <= n*2:
        if q1_sum < q2_sum:
            now = queue2.popleft()
            queue1.append(now)
            q2_sum-=now;q1_sum+=now
        elif q1_sum > q2_sum:
            now = queue1.popleft()
            queue2.append(now)  
            q2_sum+=now;q1_sum-=now
        # 두 큐의 합이 동일하면 count 반환
        else:
            return count
        if now > (q1_sum + q2_sum) / 2:return -1 
        count+=1
    return -1