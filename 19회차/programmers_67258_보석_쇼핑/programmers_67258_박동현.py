# gems를 순회하면서 dict로 접근, set로 개수 계산
def solution(gems):
    answer = []
    # target : 모든 보석 종류의 개수
    target=len(set(gems))
    ans_dict = dict()
    
    cnt = 0
    check = False
    length = float('inf')
    for gem in gems:
        cnt +=1
        ans_dict[gem] = cnt
    
        if not check and target == len(ans_dict.keys()) : check = True
        
        if check :
            if answer and answer[0] < ans_dict[gem] < answer[1] : continue
            maxv=max(ans_dict.values())
            minv=min(ans_dict.values())
            if maxv-minv<length:
                answer = [minv,maxv]
                length = maxv-minv
    return answer

#### 이건 효율성 11-15 시간초과

## 카운터는 그냥 신임
from collections import Counter

def solution(gems):
    num = len(set(gems))
    ret = []

    left = 0
    counter = Counter()
    for right in range(len(gems)):
        counter[gems[right]] += 1
        right += 1
        while len(counter) == num:
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
            ret.append([left, right])

    return sorted(ret, key = lambda x: (x[1]-x[0], x[0]))[0]