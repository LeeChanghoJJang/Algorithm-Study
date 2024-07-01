def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        a = list(format(arr1[i], 'b'))
        if len(a) < n:
            a = ['0'] * (n-len(a)) + a

        b = list(format(arr2[i], 'b'))
        if len(b) < n:
            b = ['0'] * (n-len(b)) + b

        tmp = ''
        for j in range(n):
            if int(a[j]) or int(b[j]):
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))