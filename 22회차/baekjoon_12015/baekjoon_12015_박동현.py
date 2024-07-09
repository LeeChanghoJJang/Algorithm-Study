# 뭐임 이게
def bs(num):
    start,end = 0,len(LIS)-1
    while start<=end:
        mid = (start+end) //2
        if LIS[mid] == num: return mid
        if LIS[mid] < num: start = mid+1
        else : end = mid-1
    return start

N = int(input())
arr = [*map(int,input().split())]

LIS = [arr[0]]

for item in arr:
    if LIS[-1] <item:
        LIS.append(item)
    else :
        LIS[bs(item)] = item
print(LIS)
print(len(LIS))
        