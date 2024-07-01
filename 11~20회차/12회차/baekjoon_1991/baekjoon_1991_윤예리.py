import sys
input = sys.stdin.readline

# 전위순회
def find1(x):
    result1.append(chr(x+64))
    if left[x]:
        find1(left[x])
    if right[x]:
        find1(right[x])

# 중위순회
def find2(x):
    if left[x]:
        find2(left[x])
    result2.append(chr(x+64))
    if right[x]:
        find2(right[x])

# 후위순회
def find3(x):
    if left[x]:
        find3(left[x])
    if right[x]:
        find3(right[x])
    result3.append(chr(x + 64))

n = int(input())
par = [0] * (n+1)
left = [0] * (n+1)
right = [0] * (n+1)

# ord('A') == 65
# chr(65) == 'A'

for _ in range(n):
    s1, s2, s3 = map(str, input().split())
    if not s2 == '.':
        left[ord(s1)-64] = ord(s2)-64
        par[ord(s2) - 64] = ord(s1) - 64
    if not s3 == '.':
        right[ord(s1)-64] = ord(s3)-64
        par[ord(s3) - 64] = ord(s1)-64

result1=[]
find1(1)
print(*result1, sep='')
result2=[]
find2(1)
print(*result2, sep='')
result3=[]
find3(1)
print(*result3, sep='')