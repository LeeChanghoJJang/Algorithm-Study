# 비밀지도 lv1

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]

arr2 = [27 ,56, 19, 14, 14, 10]



def solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = format(arr1[i], f'0{n}b')
        arr2[i] = format(arr2[i], f'0{n}b')

    answer = [[' '] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1':
                answer[i][j] = '#'
            if arr2[i][j] == '1':
                answer[i][j] = '#'

    for i in range(n):
        answer[i] = ('').join(answer[i])

    return answer


print(solution(n, arr1, arr2))

# ["#####","# # #", "### #", "# ##", "#####"]