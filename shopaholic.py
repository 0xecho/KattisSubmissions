input()
l=sorted([int(i) for i in input().split()],reverse=True)

l+=[0]*(len(l)-int(len(l)/3)*3)
s=0
# print(l)
for i in l[2::3]:
    s+=i

print(s)