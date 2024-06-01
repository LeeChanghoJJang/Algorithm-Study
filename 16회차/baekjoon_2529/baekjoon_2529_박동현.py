def backtrack(idx=0, visit=""):
    global maxa,mini

    if idx == N+1 :
        if int(maxa) < int(visit):
            maxa = visit
        if int(visit) < int(mini):
            mini = visit
        return 
    
    for i in arr :
        if str(i) not in visit :
            if not visit or eval(f'{visit[-1]} {opr[idx-1]} {i}'):
                backtrack(idx+1, visit+str(i))



N = int(input())
arr = list(range(10))
opr = input().split()
maxa = 0
mini = 1e10
backtrack()
print(maxa)
print(mini)