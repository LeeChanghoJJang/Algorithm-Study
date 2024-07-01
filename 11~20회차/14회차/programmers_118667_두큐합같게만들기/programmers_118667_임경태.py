# 두 큐 합 같게 만들기 (2022 KAKAO TECH INTERNSHIP)

def solution(queue1, queue2):
    # 각각 큐의 합
    sumQ1 = sum(queue1)
    sumQ2 = sum(queue2)

    # 두 큐 합이 홀수이면 불가능
    if (sumQ1 + sumQ2) & 1 : return -1

    target = (sumQ1 + sumQ2) // 2  # 타겟 합
    circleQ = queue1 + queue2      # 전체 큐
    lenQ = len(circleQ)            # 큐 길이
    left, right = 0, lenQ//2       # 포인터
    ans = 0

    # 왼쪽 포인터가 끝까지 갈 때까지 반복
    while left < lenQ:
        # 큐의 합이 타겟과 같으면 횟수 반환
        if sumQ1 == target:
            return ans
        # 큐의 합이 타겟보다 작으면 오른쪽 포인터 이동
        elif sumQ1 < target:
            sumQ1 += circleQ[right % lenQ]
            right += 1
        # 큐의 합이 타겟보다 크면 왼쪽 포인터 이동
        elif sumQ1 > target:
            sumQ1 -= circleQ[left % lenQ]
            left += 1
        # 카운트
        ans += 1

    # 왼쪽 포인터가 끝까지 갔는데도 결론이 안나면 불가능
    return -1