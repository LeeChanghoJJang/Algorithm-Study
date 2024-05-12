def solution(n, arr1, arr2):
    return [f'{int(bin(i|j)[2:]):0{n}}'.replace("1","#").replace("0"," ") for i,j in zip(arr1,arr2)]
