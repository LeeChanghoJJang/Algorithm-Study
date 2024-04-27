t = int(input())

for idx in range(t):
    size, k = map(int,input().split())
    test_case = set(range(1,size+1))
    not_test = set(map(int,input().split()))
    print(f"#{idx+1}", end=" ")
    print(*(test_case - not_test))