def calc(f,s):
    f=f[::-1]
    s=s[::-1]
    ml=max(len(f),len(s))
    f+='0'*(ml-len(f))
    s+='0'*(ml-len(s))
    c=0
    sum=''
    for i in range(ml):
        v = int(f[i])+int(s[i])+c
        c=0
        if v>9:
            v-=10
            c+=1
        sum+=str(v)
    if c:
        sum+=str(c)
    print(sum[::-1])

calc(input(),input())