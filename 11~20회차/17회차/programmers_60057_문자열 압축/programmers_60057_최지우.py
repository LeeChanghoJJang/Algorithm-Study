def solution(s):
    n = len(s)
    answer = n

    for i in range(1, n//2 + 1):
        idx = 0
        word = ""

        while idx < n:
            tmp = s[idx:idx+i]
            cnt = 1

            while tmp == s[idx+i:idx+i*2]:
                idx += i
                cnt += 1

            if cnt == 1:
                word += tmp
            else:
                word += str(cnt) + tmp

            idx += i

        answer = min(len(word), answer)

    return answer


s = 'abcabcabcabcdededededede'
print(solution(s))