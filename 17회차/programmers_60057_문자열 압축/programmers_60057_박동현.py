def solution(s):
    answer = len(s)
    # 브루트포스
    for i in range(1,answer+1):
        # 문자열을 i 사이즈만큼 나누기
        tmp = []
        txt = ""
        for char in s :
            txt += char
            if len(txt) == i:
                tmp.append(txt)
                txt = ""
        tmp.append(txt)
        # 나눠진 문자열 리스트를 압축하기
        i,res = 0,[]
        while i < len(tmp):
            cnt = 1
            while i+cnt < len(tmp) and tmp[i] == tmp[i+cnt]:
                cnt += 1
            if cnt == 1:
                res.append(tmp[i])
            else :
                res.append(("".join([str(cnt),tmp[i]])))
            i += cnt
        
        result = "".join(res)
        # 길이 비교
        if answer > len(result):
            answer = len(result)
    return answer