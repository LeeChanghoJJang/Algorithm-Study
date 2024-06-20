def backtrack(result = []) :
    if len(result) == M :
        result = list(map(lambda x : x[1], result)) 
        ans.add(tuple(result))
        return

    for i in arr :
        if i not in result :
            backtrack(result + [i])


N,M = map(int,input().split())

arr = list(enumerate(map(int,input().split()))) # enumerate로 구분
ans = set()                                     # set로 중복 제거
backtrack()

for answer in sorted(ans):                      # 정렬 후 출력
    print(*answer)