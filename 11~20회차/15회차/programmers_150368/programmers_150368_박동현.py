def solution(users, emoticons):
    answer = [0, 0]
    sale = [10, 20, 30, 40]
    discounts = []
    N = len(emoticons)
    # Q.함수를 위에 내고 싶은데요
    # A.보통 백준에서는 함수를 내도 전역변수부터 읽기 때문에 리스트를 포함한 함수를 적어도 그대로 작동하지만
    # 각각의 함수들이기 때문에 그 변수를 그대로 받아오려면 함수 내부에서 작성해야한다.
    def backtrack(idx=0, visit=[]):
        if idx == N:
            discounts.append(visit[:])
            return
        for i in sale :
            backtrack(idx+1, visit+[i])

    backtrack()

    for discount in discounts:
        cnt,ans = 0,0
        for i in users:
            ndtp = 0
            for j in range(len(discount)):

                if i[0] <= discount[j]:
                    ndtp += emoticons[j] * (100 - discount[j])/100
                
                if ndtp >= i[1]: 
                    cnt += 1
                    break
            else :
                ans += ndtp

        if cnt >= answer[0]:
            if cnt == answer[0]:
                answer[1] = max(answer[1], ans)
            else:
                answer[1] = ans
            answer[0] = cnt


    return answer