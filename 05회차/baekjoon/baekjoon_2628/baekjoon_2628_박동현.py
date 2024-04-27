N,M = map(int,input().split())
 
t = int(input())

n_list = [0,N]
m_list = [0,M]

sorted_m = []
sorted_n = []


for _ in range(t):
    way, point = map(int,input().split())
    
    if way == 0 :
        m_list.append(point)
    else :
        n_list.append(point)

m_list.sort()
n_list.sort()

for i in range(len(m_list)-1) :
    sorted_m.append(m_list[i+1]-m_list[i])

for j in range(len(n_list)-1) :
    sorted_n.append(n_list[j+1]-n_list[j])

print(max(sorted_m) * max(sorted_n))