for _ in range(int(input())):
    l=[]
    y=False
    for _ in range(int(input())):
        l.append(input())
    for i,j in zip(sorted(l)[:-1],sorted(l)[1:]):
        if j.startswith(i):
            y=True
            break
    print("NO" if y else "YES")
        
        
