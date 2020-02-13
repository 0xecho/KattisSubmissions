_,n = [int(i) for i in input().split()]

x = [int(i)for i in input().split()]

c=0
for i in x:
    if i>n:
        break
    c+=1
    n-=i
    
print(c)