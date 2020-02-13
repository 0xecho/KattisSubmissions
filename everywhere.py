T=int(input())

for i in range(T):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(input())
    print(len(set(l)))
