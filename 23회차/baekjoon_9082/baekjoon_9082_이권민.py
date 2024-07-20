import sys
input = sys.stdin.readline 
T = int(input())
for _ in range(T):    
    n = int(input())    
    num = list(map(int, input().rstrip()))    
    mine = input().strip()    
    result = 0    
    dir = [-1, 0, 1]    
    for i in range(n):        
        if i == 0:            
            if num[0] != 0 and num[1] != 0:                
                num[0] -= 1                
                num[1] -= 1                
                result += 1        
        elif i == (n-1):            
            if num[i] != 0 and num[i-1] != 0:                
                num[i-1] -= 1                
                num[i-2] -= 1               
                result += 1        
        else:            
            if num[i-1] != 0 and num[i] != 0 and num[i+1] != 0:                
                num[i-1] -= 1                
                num[i] -= 1                
                num[i+1] -= 1                
                result += 1    
    print(result)
