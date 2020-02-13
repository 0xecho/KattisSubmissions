inp=int(input())
ll=[]
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(21):
                for m in range(21):
                    for n in range(21):
                        # print(inp,i*l+j*m+k*n)
                        if i*l+j*m+k*n==inp:
                            ll=[[i,l],[j,m],[k,n]]
                            break
x={
    1:"single",
    2:"double",
    3:"triple"
}
# print(ll)
if len(ll):
    for i in ll:
        if i[0] and i[1]:
            print(x[i[0]],i[1])
else:
    print("impossible")
