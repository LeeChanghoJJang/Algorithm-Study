# 별4 동3 네2 세1
import sys

t = int(input())

for _ in range(t):
    a = list(map(int,sys.stdin.readline().strip().split()))[1:]

    b = list(map(int,sys.stdin.readline().strip().split()))[1:]

    for i in range(4,0,-1):
        if a.count(i) > b.count(i) :
            print("A")
            break
        elif a.count(i) < b.count(i) :
            print("B")
            break
    else :
        print("D")