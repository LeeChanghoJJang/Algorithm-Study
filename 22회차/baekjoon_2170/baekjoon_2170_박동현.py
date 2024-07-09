import sys
input = sys.stdin.readline


N = int(input())

# arr 을 받는데, X-Y 는 선의 시작, 끝 
# 시작점을 기준으로 가장 긴 선만 챙겨감
arr = dict()
for _ in range(N):
    x,y = map(int,input().split())
    arr[x] = max(arr.get(x,-float('inf')), y)


data = sorted(arr.items())
start = data[0][0]
end = arr[start]

ans = 0
for s,e in data:
    if s > end:
        ans += (end-start)
        start = s
    end = max(e,end)

ans += (end-start)
print(ans)