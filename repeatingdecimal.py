import sys
def do(x,y,z):
    l="0."
    for i in range(z):
        if x==0:
            l+="0"*(z-(len(l)-2))
            break
        x = int(str(x)+"0")
        while y>x:
            x = int(str(x)+"0")
            l+="0"
        l+=str(x//y)
        x%=y
    return l[:z+2]
for line in sys.stdin:
    x,y,z = [int(i)for i in line.split()]
    print(do(x,y,z))
