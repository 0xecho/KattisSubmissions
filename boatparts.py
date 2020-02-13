n,d = [int(i)for i in input().split()]
s=set()
x="paradox avoided"
for i in range(d):
    s.add(input())
    if(len(s)==n):
        x=i+1
        s.add("*"*10)
print(x)
