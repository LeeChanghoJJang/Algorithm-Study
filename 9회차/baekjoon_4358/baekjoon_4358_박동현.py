import sys

input = sys.stdin.readline

cnt = 0
dic = {}
while True:
    tree = input().strip()
    if not tree:            # 이건 좀;
        break               # 백준 입력 값 제한 없는경우 try / except EOFEerror 로 받는거 아님? 어이없네
    cnt += 1
    
    dic[tree] = dic.get(tree,0) + 1

for key,value in sorted(dic.items()):
    print(key, f"{value/cnt*100:.04f}")