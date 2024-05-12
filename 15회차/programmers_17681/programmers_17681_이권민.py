def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n-1,-1,-1):
            if arr1[i] &(1<<j) or arr2[i] & (1<<j):
                answer[i] += '#'
            else:
                answer[i] += ' '
                
        
    
    return answer
print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))