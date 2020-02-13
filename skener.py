r,c,zr,zc = [int(i) for i in input().split()]

inp=[]

for i in range(r):
    inp.append(input())

for i in inp:
    for k in range(zr):
        for j in i:
            print(j*zc,end='')
        print()