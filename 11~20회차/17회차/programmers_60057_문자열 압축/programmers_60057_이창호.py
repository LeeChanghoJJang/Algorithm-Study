def solution(s):
    result = float('inf')
    for i in range(1,len(s)+1):
        compress='';temp=s[:i];cnt=1
        for j in range(i,len(s)+i,i):
            if temp ==s[j:i+j]:
                cnt+=1
            else:
                if cnt !=1:
                    compress += f'{cnt}{temp}'
                else:
                    compress += temp
                temp = s[j:i+j]
                cnt=1
        result = min(result,len(compress))
    return result