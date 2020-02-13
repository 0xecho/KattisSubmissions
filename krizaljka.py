a,b= input().split()
x=0
bk=False
for i,j in enumerate(a):
    for k,l in enumerate(b):
        if j==l:
            x=(max(i,k),min(i,k))

            bk=True
            break
    if bk:
        break

l=[]
for i in range(len(b)):
    l.append(["."]*len(a))

for i,j in enumerate(l):
    if i==x[0]:
        l[i]=list(a)
    j[x[1]]=b[i]
    
print(*["".join(u)for u in l],sep="\n")
