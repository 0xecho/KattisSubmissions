x,y=input().split()
while int(x) or int(y):
    x="0"+x
    y="0"+y
    if len(x)!=len(y):
        if len(x)>len(y):
            y="0"*(len(x)-len(y))+y
        if len(x)<len(y):
            x="0"*(len(y)-len(x))+x

    c=0
    tc=0
    for i,j in enumerate(x[::-1]):
        i=-(i+1)
        if int(y[i])+int(j)+c > 9:
            c=1
            tc+=1
        else:
            c=0

    if tc:
        print("{} carry operation.".format(tc) if tc==1 else "{} carry operations.".format(tc))
    else:
        print("No carry operation.")
    x,y=input().split()