def bc(x,b):
    o=""
    while x:
        o+=str(x%b)
        x//=b
        
    return o[::-1] if len(o) else "0"
        
    
while 1:
    
    try:
        b,p,m = [int(i)for i in input().split()]
        if p==0:
            print(m)
        else:
            print(bc(int(str(p),b)%int(str(m),b),b))
    except Exception as e:
        
##        print(e)
        break
