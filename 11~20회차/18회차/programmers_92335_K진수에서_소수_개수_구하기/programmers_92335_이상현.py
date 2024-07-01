def convert(n, b):
    result = ""
    while n > 0:
        r = n % b
        result = str(r) + result
        n //= b
    return result

def solution(n, k):
    answer = 0
    temp = [int(num) for num in convert(n, k).split('0') if num]
    
    for num in temp:
        if num == 1:
            continue
            
        for q in range(2, int(num ** (0.5)) + 1):
            if not num % q:
                break    
        else:
            answer += 1
        
    return answer