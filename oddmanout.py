for _ in range(int(input())):
    int(input())
    inp=input().split()
    l=[]
    for i in inp:
        if i in l:
            l.remove(i)
        else:
            l.append(i)
    print("Case #"+str(_+1)+":",l[0])
