import math

for i in range(int(raw_input())):
    inp=raw_input()
    n=(int(math.sqrt(len(inp))))
    l=[]
    for i in range(len(inp)):
        l.append(inp[:n])
        inp=inp[n:]
    l=[i[::-1] for i in l if not i is '']
##    for i in range(len(l)):
    s=[None]*100
    for i in range(n):
        for j in range(n):
            try:
                s[i]+=l[j][i]
            except:
                s[i]=l[j][i]
    print ''.join([i for i in s if not i is None])
            
