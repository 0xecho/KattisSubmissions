a=input()
b=input()

ao=""
bo=""
if len(a)>len(b):
    b="0"*(len(a)-len(b))+b
if len(b)>len(a):
    a="0"*(len(b)-len(a))+a


for i,j in enumerate(a):

    if int(j)>int(b[i]):
        ao+=j
    elif int(j)<int(b[i]):
        bo+=b[i]
    else:
        ao+=j
        bo+=b[i]
print(int(ao) if ao else "YODA")
print(int(bo) if bo else "YODA")
