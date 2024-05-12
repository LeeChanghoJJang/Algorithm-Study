from itertools import product,permutations
def solution(users, emoticons):
    ans=[-1,-1]
    for permu in product([10,20,30,40],repeat=len(emoticons)):
        cnt,max_sales=0,0
        for user in users:
            tmp = sum([emt*(1-per/100) for per,emt in zip(permu,emoticons) if user[0] <= per])
            if tmp >= user[1]:cnt+=1
            else :max_sales+=tmp
        if (ans[0]<cnt) or (ans[0]==cnt and ans[1]<max_sales):
            ans=[cnt,max_sales]
    return ans
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users,emoticons))

def solution2(users,emoticons):
    ans =[-1,-1]
    # 할인율의 모든 조합을 emoticon의 갯수만큼 구함(중복 순열)
    for pers in product([10,20,30,40],repeat=len(emoticons)):
        cnt, max_sales=0,0
        for user in users:
            tmp = sum([em * (1-per/100) for per, em in zip(pers,emoticons) if user[0] <= per])
            if tmp >= user[1]: cnt+=1
            else: max_sales+=tmp
        # cnt와 max_sales가 작으면 갱신
        if (ans[0] < cnt) or (ans[0]==cnt and ans[1] < max_sales):
            ans = [cnt,max_sales]
    return ans

def solution3(users,emoticons):
    ans = [-1,-1]
    for pers in product([10,20,30,40],repeat=len(emoticons)):
        cnt, max_sales = 0,0
        for user in users:
            tmp = sum([em * (1-per/100) for per,em in zip(pers,emoticons) if user[0] <= per])
            if tmp >= user[1]: cnt+=1
            else: max_sales+=tmp
        if ans[0] < cnt or (ans[0]==cnt and ans[1] < max_sales):
            ans = [cnt, max_sales]
    return ans
print(solution3(users,emoticons))
