from math import *
for _ in range(int(input())):
    inp =input()
    x=ceil(sqrt(len(inp)))

    inp = inp + "*"*(int(x*x-len(inp)))

    l=[]
    for i in range(0,len(inp),x):
        l.append([*inp[:x]])
        inp = inp[x:]
    
    l=[*zip(*l)]

    for i in l:
        for j in i[::-1]:
            if not j == '*':
                print(j,end='')
    print()