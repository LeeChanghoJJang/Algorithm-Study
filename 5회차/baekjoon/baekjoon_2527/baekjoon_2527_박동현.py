for _ in range(4):
    x1,y1,x2,y2, a1,b1,a2,b2 = map(int,input().split())

    # D     (다 안맞을 경우)
    if a1 > x2 or x1> a2 or y1 > b2 or b1 > y2 :
        print("d")
    # C     (두 점이 다 겹치는 경우)
    elif (x1==a2 or x2==a1) or (y2==b1 or b2==y1):
        if  (x1==a2 or x2==a1) and (y2==b1 or b2==y1):
            print("c")
        # B (한 점은 겹치는데 두 점이 겹치는건 아닌 경우)
        else :
            print("b")
    # A (서로 범위를 벗어난 것도 아니고, 점이 겹치는 것도 아닌 경우)
    else :
        print("a")