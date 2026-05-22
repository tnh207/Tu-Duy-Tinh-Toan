for i in range(1, 1000000000):
    a,b=map(int,input().split())
    if a>0 and b>0 and a<=b:
        print(a,b)
        break
    continue