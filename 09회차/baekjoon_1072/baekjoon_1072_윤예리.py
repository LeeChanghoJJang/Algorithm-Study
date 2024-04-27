x, y = map(int, input().split())
z = int((100*y)/x)

'''
100*(y+k) / (x+k) = z+1
k = (xz + x - 100 * y) / (99-z)
v1 = 99-z
v2 = (xz + x - 100 * y)
'''

v1 = (x*z + x - 100 * y)
v2 = 99-z

# 1. 둘의 수가 같을 때 print(-1)
if x == y:
    print(-1)
# 2. k를 구하는 식에서 분모가 음수가 될 대 print(-1)
elif z >= 99:
    print(-1)

# k가 정수가 아닐 때, 1을 더해서 print 해준다.
elif v1%v2:
    print(v1//v2+1)
# 딱 나눠 떨어지면 바로 print 해준다.
else:
    print(v1//v2)