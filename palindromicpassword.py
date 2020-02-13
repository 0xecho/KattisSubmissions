l=[]
for i in range(100000,1000000):
    if str(i)==str(i)[::-1]:
        l.append(i)

for _ in range(int(input())):
    x = int(input())

    try:
        i=0
        while x>l[i]:
            i+=1
    except:
        print(l[-1])
        continue
    if x==l[i]:
        print(x)
    elif abs(x-l[i-1]) <= abs(l[i]-x):
        print(l[i-1])
    else:
        print(l[i])

