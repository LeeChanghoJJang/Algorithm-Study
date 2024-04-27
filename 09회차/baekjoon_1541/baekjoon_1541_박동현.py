a=input()
# - 를 )-( 로 다 바꾸고, 양 옆에 () 치기
a = a.lstrip("0")

a = list(a)

for idx in range(len(a)) :
    if a[idx] in "+-" :
        while a[idx+1] == "0" :
            a[idx+1] = " "
            idx+=1
output = ""
for char in a :
    output += char
output = output.replace('-', ')-(')
output = output.replace(" ", "")

print(eval(f"({output})"))