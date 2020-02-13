x,y = [int(i)for i in input().split()]

l=[]

for i in range(x):
    ll=[]
    for j in range(y):
        inp = input()
        ll.append(inp[0].lower()+inp[1:])
    l.append(ll)

c=0

for i in range(x):
    b=True
    for j in range(y):
        if not l[i][j].islower():
            b=False
    if b:
        c+=1

print(c)
