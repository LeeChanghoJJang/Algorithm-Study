def solution(s):
    min_n = 10e10
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
#         문자열 단위 지정. len(s)-단위만큼 ㄱ.
#         문자열단위 거꾸로. 절반부터.
        tem = 0
#     문자 개수
        j = 0
#     현재 문자위치
        while j < len(s):
            
            
            repeat_count = 1
            while j + i * repeat_count < len(s) and s[j:j+i] == s[j+i*repeat_count:j+i*(repeat_count+1)]:
                repeat_count += 1
            
            if repeat_count > 1:
                tem += i + len(str(repeat_count))
                j += i * repeat_count
                
            else:
                
                j += i
                if j + i >len(s)-1:
                    tem += len(s)-j+i
                    break
                else:
                    tem += i
        
        min_n = min(min_n, tem)
    
    # 압축이 불가능한 경우 원래 문자열의 길이를 반환
                
                
    return min_n if min_n != float('inf') else len(s)