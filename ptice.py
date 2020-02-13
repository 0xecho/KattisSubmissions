input()
inp = input()
a="ABC"*100
b="BABC"*100
c="CCAABB"*100
av=0
bv=0
cv=0
for i,j in zip(inp,a):
    if i==j:
        av+=1
for i,j in zip(inp,b):
    if i==j:
        bv+=1
for i,j in zip(inp,c):
    if i==j:
        cv+=1
m=max(av,bv,cv)
print(m)
if av==m:
    print("Adrian")
if bv==m:
    print("Bruno")
if cv==m:
    print("Goran")
