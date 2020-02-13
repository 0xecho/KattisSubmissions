inp=input()
while inp!="0":
    ss=sum([int(i) for i in inp])
    i=11
    while True:
        if sum([int(i) for i in str(i*int(inp))])==ss:
            print(i)
            break
        i+=1
    inp=input()
            
