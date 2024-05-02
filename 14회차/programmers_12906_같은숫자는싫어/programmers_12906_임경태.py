# 같은 숫자는 싫어 (스택/큐)

def solution(arr):
    ans = [arr[0]]
    for n in arr:
        if n != ans[-1]:
            ans.append(n)
    return ans