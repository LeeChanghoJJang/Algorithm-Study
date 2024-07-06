    
def solution(n, info):
    max_value = -1
    answer = []

    def cal(appeach, lion):
        a_score, l_score = 0, 0
        for i in range(11):
            if appeach[i] == lion[i] == 0: continue
            elif appeach[i] > lion[i]:
                a_score += 10 - i
            else:
                l_score += 10 - i
        return a_score, l_score
    
    def dfs(lion=[], idx=0):
        nonlocal max_value,answer
        
        if idx == 11:
            a, l = 0, 0
            if sum(lion) == n:
                a, l = cal(info, lion)
            elif sum(lion) < n:
                lion[-1] += (n - sum(lion))
                a, l = cal(info, lion)
            else:
                return
            if a < l:
                if max_value < (l-a):
                    max_value = (l-a)
                    answer = [lion[:]]
                elif max_value == (l-a):
                    answer.append(lion[:])
            return
        
        lion.append(info[idx]+1)
        dfs(lion, idx+1)
        lion.pop()
        
        lion.append(0)
        dfs(lion, idx+1)
        lion.pop()
    
    dfs()
    if not answer: return [-1]

    answer.sort(key=lambda x: x[::-1], reverse=True)    
    return answer[0]