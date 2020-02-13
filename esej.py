from time import time
from random import *
from string import ascii_lowercase as low
st=time()
a,b=[int(i)for i in input().split()]

s=set()
c=1
n=2
if b==1:
    s.add(low[b])
else:
    while len(s) < b:
        for _ in range(20):
            x=list(low[:min(14,b)])
            if len(x)>1 and len(x)<15:
                shuffle(x)
                x="".join(x)
                s.add(x)
        # print(len(s))
c=0
for i in s:
    c+=1
    print(i,end=" ")
    if c==b:
        break
# print(time()-st)