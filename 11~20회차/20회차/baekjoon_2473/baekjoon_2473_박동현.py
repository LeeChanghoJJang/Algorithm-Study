N = int(input())

arr = list(map(int,input().split()))
arr.sort()
result = float('inf')
ans = []
for mid in range(N):
    left = mid +1
    right = N-1
    while left < right : 
        tmp = arr[left] + arr[mid] + arr[right]

        if result > abs(tmp) :
            result = abs(tmp)
            ans = [arr[left], arr[mid], arr[right]]

        if tmp == 0 :
            exit(print(*sorted(ans)))
        
        elif tmp > 0 :
            right -=1

        else :
            left +=1

print(*sorted(ans))