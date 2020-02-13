import string
inp=input().split()
while inp!=['0']:
    old=string.ascii_uppercase+"_."
    new=old[int(inp[0]):]+old[:int(inp[0])]
    trans = str.maketrans(old,new)
    print(inp[1].translate(trans)[::-1])
    inp=input().split()
