from copy import deepcopy   
max_diff = 0
answer = []

def dfs(info,shoot,n,i):
    global answer, max_diff
    if i == 11:
        if n!= 0:
            shoot[10] = n
        score_diff = calcDiff(info,shoot)
        if score_diff <= 0:
            return
        result = deepcopy(shoot)
        if score_diff > max_diff:
            max_diff = score_diff
            answer = [result]
            return
        
        if score_diff == max_diff:
            answer.append(result)
        return
    if info[i] < n:
        shoot.append(info[i]+1)
        dfs(info, shoot, n-info[i]-1, i+1)
        shoot.pop()
        
    shoot.append(0)
    dfs(info,shoot,n,i+1)
    shoot.pop()
    
def calcDiff(info,shoot):
    enemyScore, myScore = 0,0
    for i in range(11):
        if (info[i], shoot[i]) == (0,0):
            continue
        if info[i] >= shoot[i]:
            enemyScore += 10 - i
        else:
            myScore += (10 - i)
    
    return myScore - enemyScore

def solution(n,info):
    global answer, max_diff
    dfs(info, [], n, 0)
    if answer == []:
        return [-1]
    answer.sort(key=lambda x:x[::-1], reverse = True)
    return answer[0]